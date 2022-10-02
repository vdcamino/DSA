# Store the elements and their distances in a min heap, then pop k elements from the heap
# time complexity = O(n log(k))
# space complexity = O(n)
# better solution would be to implement a max heap and, if the size of the heap exceeds k, pop from the heap
# this second solution would also be O(n log(k)) but the space complexity would be only O(k)

import heapq
from heapq import heappop
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use min heap to retrieve the smallest k elements
        inputs = []
        for coord in points:
            dist = math.sqrt(coord[0] ** 2 + coord[1] ** 2)
            inputs.append([dist, coord[0], coord[1]])
        # convert list into min heap
        heapq.heapify(inputs)
        # result list
        res = []
        i = 0
        while i < k:
            aux = heappop(inputs)
            res.append([aux[1], aux[2]])
            i += 1
        return res
