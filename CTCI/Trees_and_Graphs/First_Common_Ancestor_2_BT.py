class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# traverse the tree with dfs
# when you hit one of the two desired nodes, there are three possibilities
# 1. the other node is on the other side of the root: in this case, root is the lca
# 2. the other node is a left child of this node you hit: if this is the case, the node you hit is the lca
# 3. the other node is a right child of this node you hit: if this is the case, the node you hit is the lca


# solution 1
class Solution:
    def lca(self, root, p, q):
        # found nothing, base case
        if not root:
            return None

        # if the current node matches one of the targets, we return the value of that node to the recursive call
        if root == p or root == q:
            return root

        l = self.lca(
            root.left, p, q
        )  # l will value p or q if one of these nodes was found during the precedent stack calls
        r = self.lca(
            root.right, p, q
        )  # r will value p or q if one of these nodes was found during the precedent stack calls

        # the first node that receives a non null value for both l and r in its stack call will be the lca
        if l and r:
            return root
            # if the other node was below the first node that was found on the right/left subtree, it will not be found
            # during the remaining stack calls (because we made the break when we found the first one)
            # so we return the only non null value that we have in our pointers
        else:
            return l or r


# solution 2
# class Solution:
#     def lca(self, root, p, q):
#         self.ans = None

#         def dfs(node):
#             # found nothing/hit the end of a branch, base case
#             if not root:
#                 return False
#             # left recursion
#             left = dfs(node.left)
#             # right recursion
#             right = dfs(node.right)
#             # check if the current node is equal to one of the targets
#             cur = node == p or node == q
#             # if any of the two flags was passed to this node's stack call, then this is the lowest common ancestor
#             if (left and right) or (left and cur) or (right and cur):
#                 self.ans = node
#                 return
#             # return true for this call if either of the 3 flags are true
#             return left or right or cur

#         # traverse the tree
#         dfs(root)
#         return self.ans
