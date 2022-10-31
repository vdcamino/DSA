# Approach 1:


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid, nextStart = self.getMid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(nextStart)

        return root

    def getMid(self, head):
        # init pointers
        slow, fast = head, head
        prev_slow = ListNode(-1)
        prev_slow.next = slow

        # find middle with two pointers technique, slow end in the middle or last of left half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev_slow = prev_slow.next

        # separate middle node from the two halves
        nextStart = slow.next
        prev_slow.next = None
        slow.next = None
        return slow, nextStart


# Approach 2:


class Solution:
    def findSize(self, head):
        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1
        return n

    def sortedListToBST(self, head):
        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)
