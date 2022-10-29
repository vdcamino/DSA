class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def morris_inorder(root):
    res = []
    cur = root
    while cur:
        if not cur.left:
            # if there is no left subtree, you can process the current root and go the right subtree (left -> root -> right)
            res.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                # find rightmost element of left subtree
                prev = prev.right
            if not prev.right:
                # set up a thread so you can come back to the root later on
                prev.right = cur
                # now you can go left
                cur = cur.left
            else:
                # undo the thread the second time you find this rightmost node
                prev.right = None
                # it is the time to precess the root and go to the right because inorder: left --> root --> right
                res.append(cur.val)
                cur = cur.right
    return res


if __name__ == "__main__":
    # init tree, node1 is the root
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(2)
    node4 = TreeNode(1)
    node5 = TreeNode(7)
    node1.left = node2
    node2.left = node3
    node1.right = node4
    node4.right = node5

    inorder = morris_inorder(node1)
    print(inorder)
