# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# postorder traversal: left -> right -> cur


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.p_found, self.q_found = False, False

        def dfs(node):
            if not node:
                return False

            r = dfs(node.right)
            l = dfs(node.left)
            cur = node == p or node == q

            if node == p:
                self.p_found = True
                return node
            elif node == q:
                self.q_found = True
                return node

            if (r and l) or (r and cur) or (l and cur):
                return node
            return l or r or cur

        self.ans = dfs(root)
        return self.ans if self.p_found and self.q_found else None
