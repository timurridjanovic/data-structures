### Not done ####

graph = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 11], 4: [1, 5, 7], 
    5: [2, 4, 6, 8], 6: [5, 9, 10], 7:[4, 13], 8: [5, 14], 
    9: [6, 12], 10: [6, 11], 11: [3, 10], 
    12: [9], 13: [7, 14], 14: [8, 13]
}


class Graph(object):
    def __init__(self, start, end, graph):
        available = []
        visited = []
        paths = []
        
        available.append(start)
        
        while len(available) > 0:
            currentNode = available.pop()
            visited.append(currentNode)
            paths.append([currentNode])
            
            if currentNode == end:
                print 'yay'
                break
            
            neighbors = graph[currentNode]
            neighbor = graph[currentNode][0]
            if len(neighbors) == 1 and neighbors[0] is not end:
                
            
            if neighbor in visited:
                continue
            elif neighbor not in available:
                available.append(neighbor)
                
            if len(available) <= 0:
                
                
                    
                    
                        
        
            
