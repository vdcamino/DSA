# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # Iterative
        result = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result       
    
    # Recursion 
        result = []
        def inOrderRec(root):
            if not root:
                return 
            inOrderRec(root.left)
            result.append(root.val)
            inOrderRec(root.right)   
        inOrderRec(root)
        return result