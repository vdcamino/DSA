# algorithm to check if a binary tree is balanced
# a binary tree is balanced if the heights of the subtrees of any node never differ by more than one
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# naive solution = traverse the tree and, for each node, compute the height of its subtree (dfs on left and right side)
# time complexity = O(N*log(N)) where N is the numebr of nodes in the tree
# each node is "touched" once per node above it
def getHeightRec(root):
    # base case
    if root == None:
        return -1
    return max(getHeightRec(root.left), getHeightRec(root.right)) + 1


# naive recursion where we verify if each node is balanced (one by one)
def isBalancedRec(root):
    # base case
    if root == None:
        return True
    heightDiff = getHeightRec(root.left) - getHeightRec(root.right)
    if abs(heightDiff) > 1:
        return False
    return isBalancedRec(root.left) and isBalancedRec(root.right)


# smart solution in which we store the heights of the left and right subtress that we just inspected
# time complexity = O(N), where N is the number of nodes in the tree
# space complexity = O(H), where H is the height of the tree
def isBalanced_KeepingHeights(root):
    # declare nested dfs function
    def dfs(root):
        if not root:
            return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1] <= 1)
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]


if __name__ == "__main__":
    # init tree nodes, node1 = root
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(47)
    node5 = TreeNode(454)
    node6 = TreeNode(42)
    node1.left = node2
    node1.right = node3
    node2.right = node6
    node3.left = node5
    node5.left = node4
    # print(isBalancedRec(node1))
    print(isBalanced_KeepingHeights(node1))
