#Hash Table in Python

class HashTable(object):
    def __init__(self, buckets):
        self.buckets = buckets
        self.table = []
        for e in range(0, buckets):
            self.table.append([])

    def createHash(self, key):
        index = 0
        self.key = key
        for e in key:
            index = (index + ord(e)) % self.buckets
        return index

    def get(self, key):
        n = self.createHash(key)
        for e in self.table[n]:
            if e[0] == key:
                return e[1]
        return "your key is not present in the hash table"

    def setKey(self, key, value):
        n = self.createHash(key)
        self.table[n].append([key, value])
        return self.table
    
hashTable = HashTable(30)

hashTable.setKey("house", "burn")
hashTable.setKey("a", "1")
hashTable.setKey("b", "2")
hashTable.setKey("c", "3")
hashTable.setKey("d", "4")
hashTable.setKey("e", 5)
hashTable.setKey("f", 6)
hashTable.setKey("g", 7)
hashTable.setKey("h", {'a':1})


print hashTable.get("house")
print hashTable.get("a")
print hashTable.get("g")
print hashTable.get("timur")
