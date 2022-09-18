# # algorithm to find the "next" node in a binary search tree
# # next in a in order traversal
# #      3
# #    /   \
# #   2     5
# #  / \      \
# # 1   2.5    7
# #           / \
# #          6   10
# # in order traversal always goes left subtree -> current node -> right subtree
# # so the next node to print should be the left most node in the right subtree of the given node
# # special case = if the node does not have a right subtree (for instance, the 2.5 node)
# # in this case we must pick up where we left off with the node's parent (the 2 in the 1.5 case)
# #   case 1 = if the node was to the left of its parent (for instance, the node 6),
# #       then the next node we should traverse will be its parent
# #           this is because in order traversal = left subtree -> current node -> right subtree
# #   case 2 = if the node was to the right of its parent (for instance, the node 1.5)
# #       then we have already traversed the parent's subtree
# #       in this case, we need to traverse upwards from the parent until we find a node x that
# #       we have not fully traversed
# #


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None


# def successor(root, node):


# if __name__ == "__main__":
#     # init tree
#     node1 = TreeNode(3)
#     node2 = TreeNode(2)
#     node3 = TreeNode(5)
#     node4 = TreeNode(6)
#     node5 = TreeNode(10)
#     node1.left = node2
#     node1.right = node3
#     node3.right = node4
#     node4.right = node5
#     print(successor(node1, node5))
