# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        toFind = set(nodes)

        def dfs(node):
            if not node:
                return None

            if node in toFind:
                return node

            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node
            else:
                return l or r

        ans = dfs(root)
        return ans
