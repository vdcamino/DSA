class Intervals:
    # De Morgan to check if two intervals overlap (see no overlap condition and reverse it)
    # Sorting the input array is frequently useful

    def do_overlap(self, interval1, interval2):
        return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]

    def merge_intervals(self, interval1, interval2):
        return [min(interval1[0], interval2[0]), min(interval1[1], interval2[1])]

    def get_conflict_period(self, interval1, interval2):
        return [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
