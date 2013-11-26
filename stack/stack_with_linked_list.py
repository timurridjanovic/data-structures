from linked_list.linked_list import LinkedList, Node

class Stack(object):
	def __init__(self):
		self.stack = LinkedList()

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		if self.stack.length():
			return self.stack.retrieve(self.stack.length() - 1)
		else:
			raise Exception("List is Empty")

	def isEmpty(self):
		return not self.stack.length()

	def size(self):
		return self.stack.length()


stack = Stack()

stack.push("Timmy")
stack.push("hello")
stack.push("babu")
print stack.size()
