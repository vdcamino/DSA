class MinQueue:
    def __init__(self):
        self.queue = collections.deque([])
        self.minQueueHelper = collections.deque([])

    # add an element to the right of the queue
    def enqueue(self, val):
        while self.minQueueHelper and self.minQueueHelper[-1] > val:
            self.minQueueHelper.pop()
        self.minQueueHelper.append(val)
        self.queue.append(val)

    # remove element from the left of the queue
    def dequeue(self):
        val = self.queue[0]
        self.queue.popleft()

        if self.minQueueHelper[0] == val:
            self.minQueueHelper.popleft()

    # return the value at extreme left of the queue
    def getMin(self):
        return self.minQueueHelper[0]


class MaxQueue:
    def __init__(self):
        self.queue = collections.deque([])
        self.maxQueueHelper = collections.deque([])

    # add an element to the right of the queue
    def enqueue(self, val):
        while self.maxQueueHelper and self.maxQueueHelper[-1] < val:
            self.maxQueueHelper.pop()
        self.maxQueueHelper.append(val)
        self.queue.append(val)

    # remove element from the left of the queue
    def dequeue(self):
        val = self.queue[0]
        self.queue.popleft()

        if self.maxQueueHelper[0] == val:
            self.maxQueueHelper.popleft()

    # return the value at extreme left of the queue
    def getMax(self):
        return self.maxQueueHelper[0]


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        minQueue = MinQueue()
        maxQueue = MaxQueue()
        best = -inf

        for r in range(len(nums)):
            minQueue.enqueue(nums[r])
            maxQueue.enqueue(nums[r])

            while maxQueue.getMax() - minQueue.getMin() > limit:
                maxQueue.dequeue()
                minQueue.dequeue()
                l += 1

            best = max(best, r - l + 1)

        return best
