class MyStack:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.rearrange_queue_except_top()
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def rearrange_queue_except_top(self):
        n = len(self.queue)
        while n > 1:
            cur = self.queue.popleft()
            self.queue.append(cur)
            n -= 1

    def empty(self) -> bool:
        return len(self.queue) == 0
