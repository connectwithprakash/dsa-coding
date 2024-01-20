# Attempt 1: Simple approach using merge interval algorithm O(nlogn)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            result = []
            # Sort the intervals by first element of range
            # This will help us to understand the start of range
            intervals.sort(key=lambda item: item[0])
            # Variable to store the current range
            starti, endi = intervals[0]
            for interval in intervals[1:]:
                # Checks if there is an overlap between consecutive range
                if interval[0] <= endi:
                    # Based on the kind of overlap choose the end of range
                    endi = max(endi, interval[1])
                else: # If there is no overlap - separate range
                    result.append([starti, endi])
                    starti, endi = interval
            result.append([starti, endi])

            return result

        intervals += [newInterval]
        intervals = merge(intervals)

        return interval
s
