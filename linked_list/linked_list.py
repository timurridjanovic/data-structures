import copy

class LinkedList(object):
    def __init__(self, *args):
        self.currentNode = None
        for e in args:
            self.append(e)
            
    def __iter__(self):
        if self.length() is None:
            return
        for i in range(self.length()):
            if type(self.retrieve(i)) == LinkedList:
                yield self.retrieve(i).showList()
            else:
                yield self.retrieve(i) 
                
    def __getitem__(self, index):
        if self.length() is None:
            return self.showList()
        if isinstance(index, slice):
            return self.showList(index.start, index.stop)
        else: 
            if index < 0:
                index = self.length() - abs(index)
                return self.retrieve(index)
            return self.retrieve(index)  
        
    def __setitem__(self, index, value):
        if self.length() is None:
            return  
        if isinstance(index, slice):
            indexStart = self.adjustIndexStart(index.start)
            indexStop = self.adjustIndexStop(index.stop)
            for i in range(indexStart, indexStop):
                self.delete(indexStart)
            j = indexStart 
            for e in value:
                self.insert(e, j)
                j += 1    
        else:
            self.updateByIndex(value, index)     
                     
    def __repr__(self):
        return self.showList() 
        
    def __len__(self):
        return self.length() 
        
    def __add__(self, value):
        copiedList = copy.deepcopy(self)
        copiedList[copiedList.length():] = value
        return copiedList  
        
    def __radd__(self, value):
        copiedList = copy.deepcopy(self)
        copiedList[0:0] = value
        return copiedList              

    def append(self, element):
        if self.currentNode:
            newNode = Node(element, self.currentNode, None, self.currentNode.index+1)
            self.currentNode.child = newNode
        else:
            newNode = Node(element, None, None, 0)
        self.currentNode = newNode  
        
    def pop(self):
        if self.currentNode == None:
            raise Exception("List is Empty")
        else:
            pop = self.currentNode
            self.currentNode = self.currentNode.parent
            if self.length() > 0:
                self.currentNode.child = None              
            return pop.node

    def showList(self, indexStart=None, indexStop=None):
        #adjust indexStart for slicing
        indexStart = self.adjustIndexStart(indexStart)
        #adjust indexStop for slicing  
        indexStop = self.adjustIndexStop(indexStop)
        #start constructing list    
        listo = '['
        if self.currentNode == None or (indexStart == indexStop and indexStart != None): #for slicing
            return listo + ']'
        node = self.currentNode
           
        while node.index is not indexStart:
            node = node.parent      
      
        while node.index is not indexStop-1:
            if type(node.node) == LinkedList:
                listo = listo + node.node.showList() + ', '    
            else:
                listo = listo + str(node.node) + ', '
            node = node.child
        if type(node.node) == LinkedList:
            listo = listo + node.node.showList() + ']'    
        else:
            listo = listo + str(node.node) + ']'
        return listo
        
    def adjustIndexStart(self, indexStart):
        if indexStart == None:
            indexStart = 0
        if indexStart < 0:
            indexStart = self.length() - abs(indexStart)
            if indexStart < 0:
                indexStart = 0
        if indexStart > self.length():
            indexStart = self.length()
        return indexStart    
            
    def adjustIndexStop(self, indexStop):
        if indexStop == None:
            if self.length() is not None:
                indexStop = self.length()  
            else:
                indexStop = 0
        if indexStop < 0:
            indexStop = self.length() - abs(indexStop)
            if indexStop < 0:
                indexStop = self.length()
        if indexStop > self.length():                                
            indexStop = self.length()  
        return indexStop                          
        
        
    def insert(self, element, index):
        if not self.currentNode:
            return self.append(element)
        if index > self.currentNode.index:
            self.append(element)
            return
            
        self.getNodeByIndex(index)
        newNode =  Node(element, self.currentNode.parent, self.currentNode, self.currentNode.index)
        
        if self.currentNode.parent:
            self.currentNode.parent.child = newNode
        self.currentNode.parent = newNode
        
        self.goBackToFrontNode('insert')  
        
        
    def delete(self, index):
        if index > self.currentNode.index:
            raise Exception("List index is out of range")
        if index == self.currentNode.index:
            self.pop()    
        else:
            self.getNodeByIndex(index)
        
            previous = self.currentNode.parent
            next = self.currentNode.child
        
            if self.currentNode.parent:
                self.currentNode = self.currentNode.parent
                self.currentNode.child = next
        
            if self.currentNode.child:
                self.currentNode = self.currentNode.child
                self.currentNode.parent = previous
                
            self.goBackToFrontNode('delete')     

    def find(self, element):
        self.getNode(element)
        if type(self.currentNode.node) == LinkedList:
            if element == self.currentNode.node.showList():
                found = self.currentNode
        else:
            if self.currentNode.node == element:
                found = self.currentNode
            else:
                found = None
        self.goBackToFrontNode()
        return found 
        
    def update(self, element, newElement):
        """
        updates only one instance of the element in the list. Watch out for duplicates
        """
        node = self.find(element)
        index = node.index
        self.updateByIndex(newElement, index)
        
    def updateByIndex(self, value, index):
        self.delete(index)
        self.insert(value, index)   
           
    def getNode(self, element):
        if self.currentNode == None:
            raise Exception("List is Empty")    
        while self.currentNode.node != element and self.currentNode.parent != None:
            if type(self.currentNode.node) == LinkedList:
                if element == self.currentNode.node.showList():
                    return self.currentNode.node.showList()             
            self.currentNode = self.currentNode.parent
            
    def getNodeByIndex(self, index):
        if self.currentNode == None:
            raise Exception("List is Empty")
        if index > self.length():
            index = self.length()
        if index < 0:
            index = 0        
        while self.currentNode.index is not index:
            self.currentNode = self.currentNode.parent               
            
    def goBackToFrontNode(self, updateIndexes=None):
        while self.currentNode.child is not None:
            if updateIndexes == 'delete':
                self.currentNode.index -= 1  
            if updateIndexes == 'insert':
                self.currentNode.index += 1 
            self.currentNode = self.currentNode.child 
        if updateIndexes == 'delete':
            self.currentNode.index -= 1   
        if updateIndexes == 'insert':
            self.currentNode.index += 1                                  
                        
            
    def retrieve(self, index):    
        if index > self.currentNode.index:
            raise Exception("Index is out of range")
        if index < 0:
            raise Exception ("Index is out of range")    
            
        self.getNodeByIndex(index)
        node = self.currentNode
        self.goBackToFrontNode()
        return node.node   
            
               
    def length(self):
        if self.currentNode == None:
            return None
        return self.currentNode.index + 1
        
    def sort(self):
        listToSort = copy.deepcopy(self)

        while True:
            for i in range(listToSort.length()-1):
                if listToSort[i] > listToSort[i+1]:
                    listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
               
            if self.isSorted(listToSort):
                return listToSort
            
    def isSorted(self, listo):
        for i in range(listo.length()-1):
            if listo[i] > listo[i+1]:
                return False
        return True        
   
        
class Node(object):
    def __init__(self, node, parent, child, index):
        self.node = node
        self.parent = parent
        self.child = child
        self.index = index


