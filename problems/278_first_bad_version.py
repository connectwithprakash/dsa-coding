# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        while True:
            mid = (start + end)//2
            if isBadVersion(mid):
                if mid == 0:
                    break
                else:
                    if isBadVersion(mid-1):
                        end = mid - 1
                    else:
                        break
            else:
                start = mid+1

        return mid
