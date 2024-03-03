# Attempt 1: O(logn) solution
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda interval: interval[0])

        prev_interval = points[0]
        result = 1
        for interval in points[1:]:
            if interval[0] <= prev_interval[1]:
                prev_interval = max(prev_interval[0], interval[0]), min(prev_interval[1], interval[1])
            else:
                result += 1
                prev_interval = interval

        return result

