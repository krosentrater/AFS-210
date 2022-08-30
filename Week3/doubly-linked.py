from operator import index


class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        self.count += 1
        if (self.head == None):
            # First node becomes head and tail if nothing in list
            self.head = node 
            self.tail = node
        else:
            # If there is already something in list, newly made node.next is the current self.head, self.head.rev becomes the newly made node, and we set that new node as the new head.
            node.next = self.head
            self.head.prev = node
            self.head = node
        

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        # Adds conditional to see if there is anything on the list already. If not, set node to both head and tail. If not, contiune with previous code. 
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
        # Current tail.next needs to point towards the new node. New node has to point previous towards the tail. Tail now points to the new node. Increment the counter. 
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.count += 1



    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        new_node = Node(data) #? Create new node
        if (index > self.count): #? If index is the same as length of list
            raise Exception("Index out of range.") 
        elif (index < 0): #? If index is negative
            raise Exception("Index can't be negative.")
        elif (index == 0): #? If the index is equal to index of 0, add the the beginning of the list. 
            self.addFirst(data)
        elif (index == self.count): #? If index is equal to the length of the list, add the item at the end.
            self.addLast(data)
        else: #? If none of the above apply, then add at the current position.
            # Create variables for keeping track of the positions with pointers
            curr = self.head
            prev = self.head
            for n in range(index): #? Loops through the list positions
                prev = curr 
                curr = curr.next

            new_node.next = curr
            new_node.prev = prev
            curr.prev = new_node
            prev.next = new_node
            self.count += 1


    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1 
        position = 0   
        current = self.head
        while current:
            val = current.data
            if (data == val):
                return position
            current = current.next
            position += 1
        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr



words = DoublyLinkedList()

words.add("May")
words.add("the")
words.add("Force")
words.add("be")
words.add("with")
words.add("you")
words.add("!")


# print(words)
indexOfWith = words.indexOf("with")
# print(indexOfWith)
words.__setitem__(5, "us")
print(words)
words.addAtIndex('all', 5)
print(words)