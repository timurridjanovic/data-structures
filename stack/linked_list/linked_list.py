class LinkedList(object):
    def __init__(self):
        self.currentNode = None

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
            if self.length() > 1:
                self.currentNode.child = None              
            return pop.node

    def showList(self, reverse=False):
        if self.currentNode == None:
            return None
        node = self.currentNode
        while node.parent is not None:
            if reverse is True:
                print node.node, node.parent.node, node.index
            node = node.parent    
        if reverse is True:
            print node.node, node.parent, node.index
            return
                    
        while node.child is not None:
            print node.node, node.child.node, node.index
            node = node.child
        print node.node, node.child, node.index
        
        
        
    def insert(self, element, index):
        if index > self.currentNode.index:
            self.append(element)
            return
            
        while self.currentNode.index is not index:
            self.currentNode = self.currentNode.parent
        newNode =  Node(element, self.currentNode.parent, self.currentNode, self.currentNode.index)
        
        if self.currentNode.parent:
            self.currentNode.parent.child = newNode
        self.currentNode.parent = newNode
        
        while self.currentNode.child is not None:
            self.currentNode.index += 1
            self.currentNode = self.currentNode.child
        self.currentNode.index += 1   
        
        
    def delete(self, index):
        if self.currentNode == None:
            raise Exception("List is Empty")
        if index > self.currentNode.index:
            raise Exception("List index is out of range")
        if index == self.currentNode.index:
            self.pop()    
        else:
            while self.currentNode.index is not index:
                self.currentNode = self.currentNode.parent
        
            previous = self.currentNode.parent
            next = self.currentNode.child
        
            if self.currentNode.parent:
                self.currentNode = self.currentNode.parent
                self.currentNode.child = next
        
            if self.currentNode.child:
                self.currentNode = self.currentNode.child
                self.currentNode.parent = previous
                
            while self.currentNode.child is not None:
                self.currentNode.index -= 1
                self.currentNode = self.currentNode.child
            self.currentNode.index -= 1        


        
    def retrieve(self, index):
        if self.currentNode == None:
            raise Exception("List is Empty")    
        if index > self.currentNode.index:
            raise Exception("Index is out of range")
            
        node = self.currentNode
        while node.index is not index:
            node = node.parent
        return node.node   
        
        
    def loopOverList(self, operation):
        if self.currentNode == None:
            raise Exception("List is Empty")
        length = self.length()
        for i in range(length-1):
            operation(self.currentNode)
            self.currentNode = self.currentNode.parent
            
               
    def length(self):
        if self.currentNode == None:
            return None
        return self.currentNode.index + 1                 
        
        
        
class Node(object):
    def __init__(self, node, parent, child, index):
        self.node = node
        self.parent = parent
        self.child = child
        self.index = index
             
