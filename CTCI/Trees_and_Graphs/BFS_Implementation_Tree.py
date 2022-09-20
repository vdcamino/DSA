from collections import deque

# BFS implementation to traverse trees and graphs
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# example of tree
#         2
#       /   \
#     1      3
#    / \      \
#   9   4      5


# iterative implementation
def BFS(node):
    q = deque()
    q.append(node)
    while q:
        curr = q.popleft()
        print(curr.data)  # operation to perform in BFS
        if curr.right:
            q.append(curr.right)
        if curr.left:
            q.append(curr.left)


if __name__ == "__main__":
    # init tree
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    # establish links
    node2.left = node1
    node2.right = node3
    node3.right = node5
    node1.left = node9
    node1.right = node4
    # call BFS on root (node2)
    BFS(node2)
