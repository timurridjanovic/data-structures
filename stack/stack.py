class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
        return True
        
    def pop(self):
        if not self.stack:
            raise ValueError("popping empty stack")        
        return self.stack.pop()
        
         
    def peek(self):
        if not self.stack:
            raise ValueError("peeking empty stack")
        return self.stack[-1]
        
    def isEmpty(self):
        return not self.stack
        
    def size(self):
        return len(self.stack)
      
#implementing queue with 2 stacks

class Queue(object):
    def __init__(self):
        self.stack = Stack()
        self.stack2 = Stack()
    
    def push(self, element):
        self.stack.push(element)
        
        
    def pop(self):
        if not self.stack.stack and not self.stack2.stack:
            raise ValueError("popping from empty queue")
        if not self.stack2.stack:
            for i in range(self.stack.size()):
                self.stack2.push(self.stack.pop())
        popped = self.stack2.pop()
        
        return popped
        
    def peek(self):
        if not self.stack.stack and not self.stack2.stack:
            raise ValueError("peeking empty queue")
        if not self.stack2.stack:
            return self.stack.stack[0]
        return self.stack2.stack[-1]
        
    def isEmpty(self):
        return not self.stack.stack and not self.stack2.stack
        

queue = Queue()



queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.pop()

