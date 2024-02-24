# LL: Print List
# Implement a method print_list(self) that prints the linked list's elements, one per line.

#Solution:

def print_list(self):
        temp= self.head
        while temp is not None:
            print(temp.value)
            temp =temp.next
             
    