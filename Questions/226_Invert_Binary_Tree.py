# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur.left)
                stack.append(cur.right)

        return root
