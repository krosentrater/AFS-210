class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = []
        self.count = 0

    def push(self, data):
        new_node = Node(data) # Create new node
        new_node.next = self.top # Links the newly created node's next to current self.top
        self.top = new_node # Sets the new node to current top of stack
        self.count += 1 # Increments counter
    
    def pop(self):
        if (self.top == None):
            raise Exception("Stack is empty.")
        else:
            remove_node = self.top # removed node is current self.top
            self.top = self.top.next # Sets the new self.top to the next one in the stack
            remove_node.next = None # Removes the link so there is no next for node
            self.count -= 1 # Decrements counter
            return remove_node.data # Returns the data of the removed node
    
    def size(self):
        return self.count

    def isEmpty(self):
        if (self.top == None) and (self.count == 0):
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty.")
        else:
            return self.top.data

    def iter(self):
        current = self.top
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr




class Queue:
    def __init__(self):
        self.queue = []
        self.count = 0
        
    def enqueue(self, data):
        new_node = Node(data) # Creates new node
        self.queue.insert(0, new_node) # Inserts every new node in the end of the queue
        self.count += 1 # Increments counter

    def dequeue(self):
        self.count -= 1 # Decrements counter
        return self.queue.pop() # Removes the last item from the queue

    def size(self):
        return self.count

    def isEmpty(self):
        if (self.queue == None) and (self.count == 0):
            return True
        else:
            return False
    
    def peek(self):
        indexOfLastItem = self.count
        return self.queue[indexOfLastItem].data


    
    

queue = Queue()

stack = Stack()