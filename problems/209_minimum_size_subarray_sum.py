# Attempt 1: Brute-force O(n^2) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        for window_len in range(1, n+1):
            for idx in range(n-window_len+1):
                if sum(nums[idx:idx+window_len]) >= target:
                    return window_len

        return 0


# Attempt 2: Divide and Conquer Solution but not efficient in finding sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def divide_and_conquer(target, nums):
            if len(nums) == 1:
                if nums[0] >= target:
                    return 1
                else:
                    return 0

            left = divide_and_conquer(target, nums[:-1])
            right = divide_and_conquer(target, nums[1:])
            
            if (left > 0) and (right > 0):
                return min(left, right)
            elif (left > 0):
                return left
            elif (right > 0):
                return right
            elif sum(nums) >= target:
                return len(nums)
            else:
                return 0

        min_size_sub_array, _ = divide_and_conquer(target, nums)

        return min_size_sub_array

