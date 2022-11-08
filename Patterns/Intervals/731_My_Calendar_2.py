class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        new_interval = Node(start, end)
        for overlap in self.overlaps:
            if self.do_overlap(new_interval, overlap):
                return False
        for interval in self.calendar:
            if self.do_overlap(new_interval, interval):
                new_overlap_start = max(new_interval.start, interval.start)
                new_overlap_end = min(new_interval.end, interval.end)
                new_overlap = Node(new_overlap_start, new_overlap_end)
                self.overlaps.append(new_overlap)
        self.calendar.append(new_interval)
        return True

    def do_overlap(self, interval1, interval2):
        return interval1.end > interval2.start and interval2.end > interval1.start
