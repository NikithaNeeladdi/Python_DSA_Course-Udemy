class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None
 
class BinarySearchTree:
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
                
    def contains(self,value):
        if self.root is None:
            return False
        if value == self.root.value:
            return True
        temp = self.root
        while(True):
            if value == temp.value:
                return True
            if value > temp.value:
                if temp.right is None:
                    return False
                elif temp.right == value: 
                    return True
                temp = temp.right
            if value < temp.value:
                if temp.left is None:
                    return False
                elif temp.left == value:
                    return True
                temp = temp.left
            
                    
"""
BST Contains traversal
if tree is empty -> return false 
if value == root -> return True 
temp = self.root
loop :
if value > temp or value < temp :
    if right subtree is empty -> return false 
    else: temp = temp.right
    if left subtree is empty -> return false 
    else: temp = temp.left
    

"""
        
    
            
    
    
my_tree = BinarySearchTree()

print(my_tree.root)
BinarySearchTree.insert(my_tree,47)
BinarySearchTree.insert(my_tree,27)
BinarySearchTree.insert(my_tree,57)
BinarySearchTree.insert(my_tree,17)
BinarySearchTree.insert(my_tree,77)
BinarySearchTree.insert(my_tree,7)
print(my_tree.root)
print(BinarySearchTree.contains(my_tree,787))
 


"""
Binary serach tree Trvaersals
Insertion:
    cretae a node for the new value
    If the tree is empty then make the node as root return the root
    temp = self.root
    While loop :
        if val == Root value : return false 
        # compare the value with root:
            if the val > R : Right subtree or val < R : Left Subtree
                if None insert the value or compare the val with root 
"""


