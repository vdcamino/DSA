# Python program to print nodes of extreme corners
# of each level in alternate order

# Utility class to create a node
class Node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None


# Utility function to create a tree node
def newNode(data):

    temp = Node(0)
    temp.data = data
    temp.left = temp.right = None
    return temp


# Function to print nodes of extreme corners
# of each level in alternate order
def printExtremeNodes(root):

    if root == None:
        return

    # Create a queue and enqueue left and right
    # children of root
    q = []
    q.append(root)

    # flag to indicate whether leftmost node or
    # the rightmost node has to be printed
    flag = False
    while len(q) > 0:

        # nodeCount indicates number of nodes
        # at current level.
        nodeCount = len(q)
        n = nodeCount

        # Dequeue all nodes of current level
        # and Enqueue all nodes of next level
        while n > 0:
            n = n - 1
            curr = q[0]

            # Enqueue left child
            if curr.left != None:
                q.append(curr.left)

            # Enqueue right child
            if curr.right != None:
                q.append(curr.right)

            # Dequeue node
            q.pop(0)

            # if flag is true, print leftmost node
            if flag and n == nodeCount - 1:
                print(curr.data, end=" ")

            # if flag is false, print rightmost node
            if not flag and n == 0:
                print(curr.data, end=" ")

        # invert flag for next level
        flag = not flag


# Driver program to test above functions

# Binary Tree of Height 4
root = newNode(1)

root.left = newNode(2)
root.right = newNode(3)

root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(7)

root.left.left.left = newNode(8)
root.left.left.right = newNode(9)
root.left.right.left = newNode(10)
root.left.right.right = newNode(11)
root.right.right.left = newNode(14)
root.right.right.right = newNode(15)

root.left.left.left.left = newNode(16)
root.left.left.left.right = newNode(17)
root.right.right.right.right = newNode(31)

printExtremeNodes(root)


# This code is contributed by Arnab Kundu
