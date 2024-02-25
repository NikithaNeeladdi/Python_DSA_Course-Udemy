# LL: Append
# Implement the append method for the LinkedList class.

# The append method should add a new node with a given value to the end of the linked list, updating the tail attribute and the length attribute accordingly.



# Keep in mind the following requirements:



# The method should handle the cases where the list is empty and where the list already has one or more nodes.

# The method should create a new node with the given value and add it to the end of the list.

# The method should update the tail attribute of the LinkedList correctly.

# The method should update the length attribute of the LinkedList to reflect the addition of the new node.
#Solution:
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1