# this graph represents problems set forth on this website: http://gist.io/7375570 
# breadth first graph traversal

import urllib2
file = urllib2.urlopen("http://thomasballinger.com:7777/connections.txt")

graph_dict = {}

for line in file:
    row = line.split(' ')
    row = [int(row[0]), int(row[1].replace('\n', ''))]
    if row[0] in graph_dict:
        graph_dict[row[0]].append(row[1])
    else:
        graph_dict[row[0]] = [row[1]]

print 'done'            
    
    
    
graph = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 11], 4: [1, 5, 7], 
    5: [2, 4, 6, 8], 6: [5, 9, 10], 7:[4, 13], 8: [5, 14], 
    9: [6, 12], 10: [6, 11], 11: [3, 10], 
    12: [9], 13: [7, 14], 14: [8, 13]
}


class Graph(object):
    def findPath(self, start, end, graph):
        startNode = Node(start, 0)
        endNode = Node(end, 0)
        
        openList = []
        closedList = []
        
        openList.append(startNode)
        
        while len(openList) > 0:
        
            currentNode = openList.pop(0)
            
            if currentNode.node == end:
                self.reconstructPath(currentNode)
                break
                
            closedList.append(currentNode)
            neighbors = graph[currentNode.node]
            
            for neighbor in neighbors:
                neighborNode = Node(neighbor, currentNode)
                if self.isNodeInList(neighborNode, closedList):
                    continue
                                          
                elif not self.isNodeInList(neighborNode, openList):
                    openList.append(neighborNode)
                    
                    
    def reconstructPath(self, currentNode):
        path = []
        path.append(currentNode.node)
        while currentNode.parent != 0:
            path.append(currentNode.parent.node)
            currentNode = currentNode.parent
        path.reverse()    
        print path
        return path 
        
    def isNodeInList(self, node, listofNodes):
        for element in listofNodes:
            if node.node == element.node:
                return True                          
        


class Node(object):
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
        
path = Graph()

path.findPath(1, 12, graph)
#path.findPath(1, 7777, graph_dict)

#### Problem 3


