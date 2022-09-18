import math


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# recursive way
# condition 1: for each node --> current.left.val <= current.val < current.right.val
# condition 2: we must have a min and max value for each node since, albeit condition 1 == True, every BST node must be in the right place
# time complexity = O(n)
# space complexity = O(log n) due to the recursive calls (worst case = balanced binary tree)
def isBST_Rec(root):
    # pass nested function inside of isBST(root) because we need to keep track of right and left boundaries
    def valid(root, left_boundary, right_boundary):
        # base case
        if not root:
            return True
        if (root.data <= left_boundary) or (root.data > right_boundary):
            return False
        return valid(root.left, left_boundary, root.data) and valid(
            root.right, root.data, right_boundary
        )

    return valid(root, -math.inf, math.inf)


# another solution = traverse the tree in order and store each element to an array. Then, veritfy if the array is sorted
def isBST_array(root):
    BST_list = list()

    def copyBSTtoArray(root, bst_list):
        if not root:
            return
        copyBSTtoArray(root.left, bst_list)
        bst_list.append(root.data)
        copyBSTtoArray(root.right, bst_list)
        return bst_list

    BST_list = copyBSTtoArray(root, BST_list)
    for i in range(1, len(BST_list)):
        if BST_list[i] < BST_list[i - 1]:
            return False
    return True


if __name__ == "__main__":
    # init tree
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(6)
    node5 = TreeNode(10)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    node4.right = node5
    print(isBST_array(node1))
