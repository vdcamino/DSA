# Solution 1:
# TC = O(n)
# SC = O(n)
class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            if self.do_overlap((start, end), interval):
                return False
        self.intervals.append((start, end))
        return True

    def do_overlap(self, interval_1, interval_2):
        # interval = (start, end)
        return interval_1[1] > interval_2[0] and interval_2[1] > interval_1[0]


# Solution 2:
# TC = O(log(n))
# SC = O(n)
class Node:
    def __init__(self, start, end):
        self.end = end
        self.start = start
        self.left = None
        self.right = None


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book_helper(self, new_node, node):
        # check if possible to insert to the right
        if new_node.start >= node.end:
            if node.right:
                return self.book_helper(new_node, node.right)
            else:
                node.right = new_node
                return True

        # check if possible to insert to the left
        if new_node.end <= node.start:
            if node.left:
                return self.book_helper(new_node, node.left)
            else:
                node.left = new_node
                return True

        # if no insertion was possible, there is an overlap
        return False

    def book(self, start, end):
        new_node = Node(start, end)
        if not self.root:
            self.root = new_node
            return True
        return self.book_helper(new_node, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
