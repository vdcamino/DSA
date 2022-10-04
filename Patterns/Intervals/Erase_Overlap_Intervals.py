class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if self.do_overlap(intervals[i], prev):
                res += 1
                prev = min(intervals[i], prev, key=lambda x: x[1])
            else:
                prev = intervals[i]
        return res

    def do_overlap(self, int1, int2):
        return int2[0] < int1[1] and int2[1] > int1[0]
