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


    def showList(self, reverse=False):
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
        
        
    def retrieve(self, index):
        if index > self.currentNode.index:
            raise Exception("Index is out of range")
            
        node = self.currentNode
        while node.index is not index:
            node = node.parent
        return node.node   
        
        
    def loopOverList(self, operation):
        length = self.length()
        for i in range(length-1):
            operation(self.currentNode)
            self.currentNode = self.currentNode.parent
            
               
    def length(self):
        return self.currentNode.index + 1                 
        
        
        
class Node(object):
    def __init__(self, node, parent, child, index):
        self.node = node
        self.parent = parent
        self.child = child
        self.index = index
        
                
#################
##   TESTS     ## 
#################
        
newList = LinkedList()

newList.append('hello')
newList.append('man')
newList.append(435)

newList.insert(4, 1)

newList.insert('yeah', 2)
newList.insert('end', 7)

newList.insert(23232323, 0)

newList.showList()

#newList.retrieve(5)
#newList.retrieve(0)
#newList.retrieve(1)
#newList.retrieve(6)
print newList.retrieve(2)


def operation(node):
    if node.node == 'yeah':
    
        print 'oum'
        node.node = 'oulalallalalalala'
       

newList.loopOverList(operation)



newList.showList()        
