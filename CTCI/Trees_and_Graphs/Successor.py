# algorithm to find the "next" node in a binary search tree
# next in a in order traversal
# if we traverse the BST in order, the resulting list must be sorted in ascending order
#      3
#    /   \
#   2     5
#  / \      \
# 1   2.5    7
#           / \
#          6   10
# in order traversal always goes left subtree -> current node -> right subtree
# so the next node to print should be the left most node in the right subtree of the given node
# special case = if the node does not have a right subtree (for instance, the 2.5 node)
# in this case we must pick up where we left off with the node's parent (the 2 in the 2.5 case)
#   case 1 = if the node was to the left of its parent (for instance, the node 6),
#       then the next node we should traverse will be its parent
#           this is because in order traversal = left subtree -> current node -> right subtree
#   case 2 = if the node was to the right of its parent (for instance, the node 2.5)
#       then we have already traversed the parent's subtree
#       in this case, we need to traverse upwards from the parent until we find a node x that
#       we have not fully traversed
#       how do we know that we have not fully traversed x? We know that we have hit this case when
#       we move from a left node to its parent: the left node will be fully traversed,
#       but the parent is not
#
#   pseudocode:
#       def successor(node):
#           if node has a right subtree:
#               return left most child of this right subtree
#           else:
#               if node is a left child:
#                   return parent
#               else:
#                   return parent of the parent
#   if we hit the last case and climb all the way up the tree without finding a left child, this means
#   that we are at the very end of our in order traversal


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None  # only for this question...


def getLeftMostChild(node):
    if not node:
        return None
    while node.left:
        node = node.left
    else:
        return node


def inOrderSuccessor(node):
    if not node:
        return None
    # if the node has a right subtree, we return the left most child of that right subtree
    if node.right:
        return getLeftMostChild(node.right)
    else:
        q = node
        x = q.parent
        # go up until we are on left instead of right
        while x != None and x.left != q:
            q = x
            x = x.parent
        return x


if __name__ == "__main__":
    # init tree
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node2_5 = TreeNode(2.5)
    node1 = TreeNode(1)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node10 = TreeNode(10)
    # establish parents
    node3.parent = None
    node2.parent = node3
    node2_5.parent = node2
    node1.parent = node2
    node5.parent = node3
    node6.parent = node7
    node7.parent = node5
    node10 = node7
    # establish left and right relations
    node3.right = node5
    node3.left = node2
    node2.left = node1
    node2.right = node2_5
    node5.right = node7
    node7.left = node6
    node7.right = node10

    print(inOrderSuccessor(node7).data)
