class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def printLeafs(root):
    if not root:
        return
    # leaf detected
    if not root.left and not root.right:
        print(root.val)
    printLeafs(root.left)
    printLeafs(root.right)


if __name__ == "__main__":
    myRoot = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    myRoot.left = node2
    myRoot.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node8
    node8.left = node6
    node8.right = node7

    printLeafs(myRoot)
