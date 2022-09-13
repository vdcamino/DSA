# Convert a sorted array to a balanced binary tree (BST)

# Binary tree node
class BSTNode:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def sortedArrayToBST(arr):
    if not arr:
        return None
    # Find the middle index
    mid = len(arr) // 2

    # make the middle element the root
    root = BSTNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

# A utility function to print the preorder traversal of the BST


def preOrder(node):
    if not node:
        return

    print(node.data),
    preOrder(node.left)
    preOrder(node.right)


# Test our function
arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST"),
preOrder(root)
