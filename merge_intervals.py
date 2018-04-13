# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        final_intervals = []
        last_added = Interval(-1, -1)
        for i in range (0, len(sorted_intervals) , 1):
            a = sorted_intervals[i]
            b = last_added
            if self.is_overlap(a, b):
                final_intervals.remove(b)
                new_interval = self.merge_overlapping(a, b)
                last_added = new_interval
            else:
                last_added = a
            final_intervals.append(last_added)
        return final_intervals

    def is_overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end

    def merge_overlapping(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end));
