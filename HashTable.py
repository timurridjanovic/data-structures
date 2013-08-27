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

    def set(self, key, value):
        n = self.createHash(key)
        self.table[n].append([key, value])
        return self.table
    
hashTable = HashTable(30)

hashTable.set("house", "burn")
hashTable.set("a", "1")
hashTable.set("b", "2")
hashTable.set("c", "3")
hashTable.set("d", "4")
hashTable.set("e", 5)
hashTable.set("f", 6)
hashTable.set("g", 7)
hashTable.set("h", {'a':1})


print hashTable.get("house")
print hashTable.get("a")
print hashTable.get("g")
print hashTable.get("timur")
