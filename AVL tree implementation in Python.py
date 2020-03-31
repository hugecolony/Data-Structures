# AVL tree implementation in Python
#IMPLEMENTED BY ABDULLAH P180013 FAST NUCES 
#Reference 
#https://www.programiz.com/dsa/avl-tree
#introduction-to-algorithms-third-edition by (charles E. Leiserson, Ronald L. Rivest, and Clifford Stein) pg 354

from graphviz import Digraph

def visualize_tree(tree):
    if tree is None: return 'Nothing in the tree!'
    def add_nodes_edges(tree, dot=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.attr('node', shape='circle')
            dot.node(name=str(tree), label=str(tree.val))
        
        for child in [tree.left, tree.right]:  # do for all children 
            if child is not None:
                if child == tree.left: dot.attr('node', shape='circle', style='filled', fillcolor='blue')
                if child == tree.right: dot.attr('node', shape='doublecircle', style='filled', fillcolor='pink')
                dot.node(name=str(child) ,label=str(child.val))
                dot.edge(str(tree), str(child))
                dot = add_nodes_edges(child, dot=dot)  # recursive call 

        return dot
    
    # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(tree)

    # Visualize the graph
    display(dot)
    





def print_tree(tree, level=0, label='.'): 
    print(' ' * (level*2) + label + ':', tree.val)
    for child, lbl in zip([tree.left, tree.right], ['L', 'R']):  # do for all children 
        if child is not None:
            print_tree(child, level+1, lbl)
            
##########################    
import sys

class Treenode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object): 

    def insertNode(self, root, val): 
        
        if not root: 
            return Treenode(val) 
        elif val < root.val: 
            root.left = self.insertNode(root.left, val) 
        else: 
            root.right = self.insertNode(root.right, val) 

        root.height = 1 + max(self.getHeight(root.left), 
                        self.getHeight(root.right)) 
 
        balanceFactor = self.getBalance(root) 

        if balanceFactor > 1:
            if val < root.left.val: 
                return self.rightRotate(root) 
            else:
                root.left = self.leftRotate(root.left) 
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            if val > root.right.val: 
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right) 
                return self.leftRotate(root)
            
        return root 

    def delete(self, root, val): 

        if not root: 
            return root 

        elif val < root.val: 
            root.left = self.delete(root.left, val) 

        elif val > root.val: 
            root.right = self.delete(root.right, val) 

        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 

            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 

            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                    temp.val) 

        if root is None: 
            return root 

        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 

        balanceFactor = self.getBalance(root) 

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0: 
                return self.rightRotate(root) 
            else:
                root.left = self.leftRotate(root.left) 
                return self.rightRotate(root) 


        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0: 
                return self.leftRotate(root) 
            else:
                root.right = self.rightRotate(root.right) 
                return self.leftRotate(root)

        return root 

    def leftRotate(self, z): 

        y = z.right 
        T2 = y.left 

        y.left = z 
        z.right = T2 

        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        return y 

    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 

        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        return y 

    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 

    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 

        return self.getMinValueNode(root.left) 

    def preOrder(self, root): 

        if not root: 
            return

        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
        
    def printHelper(self, currPtr, indent, last):
           if currPtr != None:
            sys.stdout.write(indent)
            if last:
                  sys.stdout.write("R----")
                  indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.val)

            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

myTree = AVL_Tree() 
root = None
nums = [33, 13, 53, 9, 21, 61, 8, 11] 

for num in nums: 
    root = myTree.insertNode(root, num)
root= myTree.delete(root,13)
visualize_tree(root)
