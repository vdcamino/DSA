# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        mini = min(p.val, q.val)
        maxi = max(p.val, q.val)
        if root.val > maxi and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < mini and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
