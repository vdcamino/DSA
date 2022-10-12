# Input:
# 	   5
# 	 /   \
# 	3     8
#  / \   / \
# 1   4 6   9

# Ouput: 1, 9, 4, 6

# I dont think there is any way to optimise the time complexity, but space complexity can be reduced down to O( Log n)
# or O(height of the tree) by keeping two stacks and alternating between them once you find a leaf node in any of the stack.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def insert_left(node, stack):
    while node:
        stack.append(node)
        node = node.left


def insert_right(node, stack):
    while node:
        stack.append(node)
        node = node.right


def printAlternateLeavesBST(root):
    stack_left = []
    stack_right = []
    insert_left(root, stack_left)
    insert_right(root, stack_right)

    reverse = False

    while stack_left and stack_right:
        if reverse:
            node = stack_right.pop()
            insert_right(node.left, stack_right)
        else:
            node = stack_left.pop()
            insert_left(node.right, stack_left)
        if not node.left and not node.right:
            reverse = not reverse
            print(node.val)


# Stack 1: Push the left node until there is None
# Stack 2: Push the right node until there is None

# Keep popping stack 1 --> add the left node until there is None for right child of popped Node
# if popped node is leaf:
# change to stack 2 and next pop from stack 2 and repeat

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    printAlternateLeavesBST(root)
