#Hash Table in Python

class HashTable(object):
    def __init__(self, buckets):
        self.buckets = buckets
        self.table = []
        self.entryNumber = 0
        self.initialBuckets = self.buckets
        for e in range(0, buckets):
            self.table.append([])

    def createHash(self, key):
        index = 0
        key = hash(str(key))
        index = key % self.buckets
        return index

    def lookup(self, key):
        bucket = self.getBucket(key)
        for e in bucket:
            if e[0] == key:
                return e[1]
        return False

    def getBucket(self, key):
        n = self.createHash(key)
        return self.table[n]

    def insert(self, key, value):
        if self.lookup(key):
            return False
        if self.entryNumber >= self.buckets/3:
            self.buckets *= 2 ## doubling buckets
            self.rehashTable()
        n = self.createHash(key)
        self.table[n].append([key, value])
        self.entryNumber += 1
        return True

    def update(self, key, value):
        bucket = self.getBucket(key)
        for e in bucket:
            if e[0] == key:
                e[1] = value
                return True
        return False

    def delete(self, key):
        if self.entryNumber <= self.buckets/6:
            self.buckets /= 2 ## dividing buckets by 2
            self.rehashTable()
        bucket = self.getBucket(key)
        for i in range(0, len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.entryNumber -= 1
                return True
        return False

    def rehashTable(self):
        keys = self.getKVPairs()
        self.table = [[] for i in range(0, self.buckets)]
        self.entryNumber = 0
        for e in keys:
            self.insert(e[0], e[1])
        return True

    def getKVPairs(self):
        return [pair for bucket in self.table for pair in bucket]

    
    def deleteAll(self):
        self.buckets = self.initialBuckets
        self.table = [[] for i in range(0, self.buckets)]
        return True
    
hashTable = HashTable(30)


hashTable.insert("house", "burn")
hashTable.insert("a", "1")
hashTable.insert("b", "2")
hashTable.insert("c", "3")
hashTable.insert("d", "4")
hashTable.insert("e", 5)
hashTable.insert("f", 6)
hashTable.insert("g", 7)
hashTable.insert("h", {'a':1})

