class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class PreOrder:
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
    def pot(self):
        results = []
        temp = self.root
        def traverse(temp):
            results.append(temp.value)
            if temp.left is not None:
                traverse(temp.left)
            if temp.right is not None:
                traverse(temp.right)
        traverse(temp)
        return results
        
        """
        
            push the current node to call stack and results array
            print the value in the result 
            check if left subtree exits
                push the left and 
            check if right subtress exists right 
                push to the call stack
            return results
        """
                
my_tree = PreOrder()
PreOrder.insert(my_tree,47)
PreOrder.insert(my_tree,27)
PreOrder.insert(my_tree,37)
PreOrder.insert(my_tree,57)
PreOrder.insert(my_tree,67)
PreOrder.insert(my_tree,77)
PreOrder.insert(my_tree,7)
print(my_tree.root)
print(PreOrder.pot(my_tree))
