""" given tree LRR'
    create a tree and node contrctoes
    traverse the tree instance
    
    creta function for traversal:
    results []
    callstack - currentnode
    if left subtress exists:
        traverse left subtree
    if right subtress exists :
        travers a right subtress
    results.append(temp.value)
        
    
"""
    
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class PostOrder:
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
    def PostOT(self):
        results =[]
        temp =
my_tree = PostOrder()
PostOrder.insert(my_tree,47)
PostOrder.insert(my_tree,27)
PostOrder.insert(my_tree,37)
PostOrder.insert(my_tree,57)
PostOrder.insert(my_tree,77)
PostOrder.insert(my_tree,97)
PostOrder.insert(my_tree,7)
PostOrder.insert(my_tree,17)
print(my_tree.root)
