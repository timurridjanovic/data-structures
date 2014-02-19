### Not done ####

graph = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 11], 4: [1, 5, 7], 
    5: [2, 4, 6, 8], 6: [5, 9, 10], 7:[4, 13], 8: [5, 14], 
    9: [6, 12], 10: [6, 11], 11: [3, 10], 
    12: [9], 13: [7, 14], 14: [8, 13]
}


class Graph(object):
	def find_path(self, start, end, graph):
        	open = [start]
       		closed = [] 
     
        	while len(open) > 0:		
            		currentNode = open.pop()
            		closed.append(currentNode)
             
            		if currentNode == end:
                		print 'yay'
				print closed
                		break
            
            		neighbors = graph[currentNode]
			for neighbor in neighbors:
				if neighbor not in closed:
					open.append(neighbor)
		   	
         

                
g = Graph()                
                    
                    
g.find_path(1, 12, graph)                        
print graph 
            
