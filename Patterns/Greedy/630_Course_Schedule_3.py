class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort input based on end_time
        courses.sort(key=lambda x: x[1])

        # used to get the course with the max duration we have taken so far
        max_heap = []
        timestamp = 0

        for duration, end_time in courses:
            # always try to take the current course
            timestamp += duration
            heapq.heappush(max_heap, -duration)

            # before it was ok, now it is not
            # so pop course with longest dureation to make it valid again
            if timestamp > end_time:
                # remember: value here is negative
                longest_duration = heapq.heappop(max_heap)
                timestamp += longest_duration

        return len(max_heap)
