"""
Binary Tree Traversal Implementation

This program demonstrates:
1. Pre-order traversal
2. In-order traversal
3. Post-order traversal
4. Level-order traversal
"""


from collections import deque



class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None



# Pre-order Traversal
# Root -> Left -> Right

def preorder(root):

    if root:

        print(root.value, end=" ")

        preorder(root.left)

        preorder(root.right)



# In-order Traversal
# Left -> Root -> Right

def inorder(root):

    if root:

        inorder(root.left)

        print(root.value, end=" ")

        inorder(root.right)



# Post-order Traversal
# Left -> Right -> Root

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.value, end=" ")



# Level-order Traversal
# Uses Queue

def level_order(root):

    if root is None:
        return


    queue = deque()

    queue.append(root)


    while queue:


        node = queue.popleft()


        print(node.value, end=" ")


        if node.left:

            queue.append(node.left)


        if node.right:

            queue.append(node.right)



# Creating Binary Tree


root = Node(1)

root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)

root.right.left = Node(6)

root.right.right = Node(7)



print("===== Binary Tree Traversal =====")


print("\nPre-order Traversal:")

preorder(root)



print("\n\nIn-order Traversal:")

inorder(root)



print("\n\nPost-order Traversal:")

postorder(root)



print("\n\nLevel-order Traversal:")

level_order(root)