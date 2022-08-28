class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
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
    
    def init(self, str):
        if (len(str) == 0):
            raise Exception("Invalid Input.")

        for i in str:
            self.push(i)



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def dequeue(self):
        if (self.head == None):
            raise Exception("Queue is empty.")
        elif (self.count == 1):
            val = self.head.data
            self.head = None
            self.tail = None
            self.count -= 1
            return val
        else:
            val = self.head.data
            self.head = self.head.next
            self.count -= 1
            return val

    def isEmpty(self):
        if (self.head is None):
            return True
        else:
            return False

    def size(self):
        return self.count

    def peek(self):
        return self.head.data

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr
    
    def init(self, str):
        if (len(str) == 0):
            raise Exception("Invalid Input.")

        for i in str:
            self.enqueue(i)

def isPalindrome(val):
    stack = Stack()
    queue = Queue()

    stack.init(val)
    queue.init(val)

    stackString = stack.__str__()
    queueString = queue.__str__()

    if (stackString == queueString):
        return True
    else:
        return False 


print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))