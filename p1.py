class Node :
    def __init__(self,value):
        self.value = value 
        self.next = None
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        print(temp.value)
        while temp.next is not None:
            print(temp.value)
            temp = temp.next
        
        
my_linked_List = LinkedList(21)
# my_linked_List = LinkedList(22)
# my_linked_List = LinkedList(23)
# my_linked_List = LinkedList(24)
# my_linked_List = LinkedList(25)
        
print(my_linked_List.print_list())
        