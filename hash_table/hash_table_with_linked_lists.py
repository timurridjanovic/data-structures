#Hash Table with my own Linked-list and sha256 implementation

from helpers.linked_list import LinkedList, Node
from helpers.sha_256 import *

class HashTable(object):
    def __init__(self, *args):
        self.table = LinkedList()
        self.numberOfKeys = 0
        initialValues = LinkedList()
        if args:
            for e in args:
                initialValues.append(e)
            self.buckets = len(initialValues) * 6
        else:
            self.buckets = 30    
        for i in range(self.buckets):
            self.table.append(LinkedList())
        for e in initialValues:
            self.insert(e[0], e[1])
                
            
    def __repr__(self):
        return self.showHash()        
            
    def __getitem__(self, key): 
        return self.lookup(key)  
        
    def __setitem__(self, key, value):
        self.insert(key, value)   
        
    def __delitem__(self, key):
        self.delete(key)           
    
    def createHash(self, key):
        hashKey = int(sha_256(str(key)), 16)
        index = int(hashKey % self.buckets)
        return index
        
    def getBucket(self, key):
        n = self.createHash(key)
        return self.table[n]
        
    def lookup(self, key):
        bucket = self.getBucket(key)
        for e in bucket:
            if e[0] == key:
                return e[1]
                
    def insert(self, key, value):       
        if self.numberOfKeys >= self.buckets/3:
            self.buckets *= 2
            self.rehashTable()
        bucket = self.getBucket(key)
        self.numberOfKeys += 1
        for e in bucket:
            if e[0] == key:
                e[1] = value
                return
        bucket.append(LinkedList(key, value))
        
    def showHash(self):
        hashTable = "{"
        if not self.table:
            return hashTable + "}"
        first = True
        for bucket in self.table:
            for e in bucket:
                if first:
                    hashTable = hashTable + str(e[0]) + ": " + str(e[1])
                    first = False
                else:
                    hashTable = hashTable + ', ' + str(e[0]) + ": " + str(e[1])    
        hashTable += "}"
        return hashTable
        
    def kvPairs(self):
        kvPairs = LinkedList()
        for bucket in self.table:
            for e in bucket:
                kvPairs.append(e)
        return kvPairs                
        
    def delete(self, key):
        bucket = self.getBucket(key)
        for i in range(bucket.length()):
            if bucket[i][0] == key:
                bucket.delete(i)
                self.numberOfKeys -= 1 
                break   
        if self.numberOfKeys <= self.buckets/6:
            self.buckets /= 2
            self.rehashTable()

                
    def rehashTable(self):
        kvPairs = self.kvPairs()
        self.table = LinkedList()
        self.numberOfKeys = 0
        for i in xrange(self.buckets):
            self.table.append(LinkedList())
        for bucket in kvPairs:
            self.insert(bucket[0], bucket[1])  
            
    def length(self):
        return self.numberOfKeys                
        

h = HashTable(('teme', 43), ('blabla', 'jsjsjs'), ('teme2', 999))


