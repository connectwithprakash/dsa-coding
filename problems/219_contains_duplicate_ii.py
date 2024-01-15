# Attempt 1: Naive approach O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for idx in range(n):
            for jdx in range(idx+1, n):
                if (nums[idx] == nums[jdx]) and ((jdx - idx) <= k):
                    return True
        return False

