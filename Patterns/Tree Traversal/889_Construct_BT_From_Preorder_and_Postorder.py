class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Global variables to keep keep track of where we are on each traversal
    preIndex, postIndex = 0, 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]):
        # Nested helper function
        def buildTreeNode():
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            if root.val != postorder[self.postIndex]:
                root.left = buildTreeNode()
            if root.val != postorder[self.postIndex]:
                root.right = buildTreeNode()
            self.postIndex += 1
            return root

        return buildTreeNode()
