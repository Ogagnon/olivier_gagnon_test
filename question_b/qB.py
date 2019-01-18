'''
Created on 17 jan. 2019 at 14:12

@author: Olivier Gagnon

Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis
and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).


N.B. Please be advised that this something I haven't done in quite some time. 
I hope I can at least show that know where I'd be going with this, what I should improve on that very basic concept.

Assumptions:

1) FCFS.
2) Data is stored and sent back as bytes. 

Priorities:

1) Have a working cache with functional multithreading for access and timer.
2) Add paging. Securize against system failures. Virtualize if needed.
3) Optimize. Improve memory with numpy arrays and a custom hashtable (more efficient on locality).
4) improve queuing priorities (reader writer problem)


'''

from queue import *
import sys

class Cache():
    def __init__(self, timeThreshold, maxMemSize):
        #thread
        self.timer = timeThreshold
        
        #This queue stores keys as they come in and adds them up at the end of the queue when reused.
        #An id number is stored in the key to differentiate occurences of the same dataKey.
        #dataKeyID is a dictionary that keeps a record of each active key and their active ID.
        #When a key is to be removed from the queue, dataKeyId is checked to see if this is the latest occurence of it in the queue.
        #If it is, it removes it, and its corresponding data in dataCache, otherwise it simply removes it in the queue. 
        self.longestIdleQueue = Queue(maxsize = 0) 
        self.dataKeyID
        
        #Eventually, keeping an inverse pointers map from data to keys would greatly add on efficiency
        self.cacheData = dict()
        self.maxMemSize = maxMemSize
        self.memLeft = maxMemSize
        
        self.userTimers = None #worker thread that times user presence in cache and kicks them out past the timeThreshold.
        
        self.users = None #Waiting Queue for reader and writers.
        
    #Resets at the beginning of the idle queue a key that was just used.
    def sendKeyStartOfQueue(self,key):
        self.longestIdleQueue.put(key + "-" + str(self.dataKeyID[key]+1))
        self.dataKeyID[key] = self.dataKeyID[key] + 1
        
    def read(self, key):
        #Get worker
        #Get lock in cacheData and frequenceQueue
        
        # Add key at the beginning of idle queue with appropriate ID
        if key in self.cacheData:
            self.sendKeyStartOfQueue(key)
            
            #Return hitted data
            return self.cacheData[key]
        else:
            
            #Return False for "miss"
            return False
        
    
    
    def hashData(self, data):
        #Plan some appropriate hash. Python hash by default.
        return hash(data)
    
    def put(self, data):
        
        myKey = self.hashData(data)
        
        #Return exception if data size exceeds max cache size. 
        #Of course, working with whole sets of data is ridiculous and paging is needed.
        if sys.getsizeof(data) > self.maxMemSize:
            return MemoryError
        else:
            #get worker
            #get lock on cacheData.
            
            #see note on reverse pointers map
            for key, value in self.cacheData.items():
                if value == data:
                    
                    #resets key idleness
                    self.sendKeyStartOfQueue(key)
                    
                    #if data already in cache, return key and move data up 
                    return key
            
            #if no hit
            if self.memLeft < sys.getsizeof(data):
                self.removeSize(sys.getsizeof(data) - self.memLeft)
            
            #give key an ID
            #put data and base key in cache
            #add key and its id to idleness queue.
            
            return myKey
        
        
    #Function to remove a given memory size from cache 
    def removeSize(self, size):
       #...
       #while size not reached, do removeLRU()
       
       return
    
    #Function to remove the least recently used data from cache.
    def removeLRU(self):
       #...
       
       #return size of block
       #update memLeft
       return 



        
        

        