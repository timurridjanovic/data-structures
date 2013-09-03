# DATA STRUCTURES: 

**Description**: Implementation of a few data structures in python.

## Hash Table:

1) You can create a new hash table object by inputing the number of buckets as a parameter:

```Python
hashTable = HashTable(30)
```

2) You can set a key and a value pair with the insert method:

```Python
hashTable.insert("key", "value")
```

3) You can retrieve the value with the lookup method:

```Python
hashTable.lookup("key")
```

4) You can update a key, value pair using the update method:

```Python
hashTable.update("key", "value")
```

5) You can delete a key using the delete method:

```Python
hashTable.delete("key")
```

6) You can completely delete the table using the deleteAll method:

```Python
hashTable.deleteAll()
```

7) You can check out all the key, value pairs by using the getKvPairs method:

```Python
hashTable.getKVPairs()
```

8) You can look at the number of inserts in the table:

```Python
hashTable.entryNumber
```

9) You can look at the number of buckets in the table:

```Python
hashTable.buckets
```

10) You can look at your table like this:

```Python
hashTable.table
```

