"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Optional[Node]":
        # Case 1: node has a right child
        # go find the leftmost node of the right subtree
        successor = None
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            successor = node
            return successor

        # Case 2: node does not have a right child
        # go find the parent from which this subtree comes
        else:
            p = node.parent
            # go up until we are done with this left subtree
            # if we went up until the root, and then null, it means that
            # we were at the rightmost node, which does not have a successor
            while p and p.val < node.val:
                p = p.parent
            return p
