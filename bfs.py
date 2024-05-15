"""
 Constructor logic:
    crete node constructor 
    cerate tree constrauctor  
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BreadthFirstSearch:
    def __init__(self):
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
    def bfs(self):
        if self.root is None:
            return False
        queue = []
        result = []
        temp = self.root
        queue.append(temp)
        while(len(queue)>0):
            temp = queue.pop(0)
            result.append(temp.value)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            
            
        return result 
        
        
        
"""
call the function with instance of tree 
queue- nodes
result -values
if tree is empty -> return False 
store the root in queue
loop-queue is empty:
    store root value in result
    store left and right nodes in queue
return the result 
"""
my_tree = BreadthFirstSearch()
BreadthFirstSearch.insert(my_tree,47)
BreadthFirstSearch.insert(my_tree,27)
BreadthFirstSearch.insert(my_tree,57)
BreadthFirstSearch.insert(my_tree,77)
BreadthFirstSearch.insert(my_tree,17)
BreadthFirstSearch.insert(my_tree,7)
BreadthFirstSearch.insert(my_tree,97)
BreadthFirstSearch.insert(my_tree,37)
print(my_tree.root.value)
print(BreadthFirstSearch.bfs(my_tree))


    
    