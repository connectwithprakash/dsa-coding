# Attempt 1: Brute-force O(n^2) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        for window_len in range(1, n+1):
            for idx in range(n-window_len+1):
                if sum(nums[idx:idx+window_len]) >= target:
                    return window_len

        return 0

