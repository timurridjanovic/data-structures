#Hash Table with my own Linked-list and sha256 implementation

from helpers.linked_list import LinkedList, Node
from helpers.sha_256 import *

class HashTable(object):
    def __init__(self, buckets):
        self.buckets = buckets
        self.table = LinkedList()
        for i in range(buckets):
            self.table.append(LinkedList())
            
    
    def createHash(self, key):
        hashKey = int(sha_256(key))
        index = int(hashKey % buckets)
        return index
        
    def getBucket(self, key):
        n = self.createHash(key)
        return self.table.retrieve(n)
        
    def lookup(self, key):
        bucket = self.getBucket(key)
        bucket.find(key)   
