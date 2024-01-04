# Attempt 1: Brute-force O(n^2) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        for window_len in range(1, n+1):
            for idx in range(n-window_len+1):
                if sum(nums[idx:idx+window_len]) >= target:
                    return window_len

        return 0


# Attempt 2: Divide and Conquer Solution -> not  O(nlogn)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def divide_and_conquer(target, nums):
            if len(nums) == 1:
                if nums[0] >= target:
                    return 1, nums[0]
                else:
                    return 0, nums[0]

            left, left_sum = divide_and_conquer(target, nums[:-1])
            right, right_sum = divide_and_conquer(target, nums[1:])
            
            if (left > 0) and (right > 0):
                if left < right:
                    return left, left_sum
                else:
                    return right, right_sum
            elif (left > 0):
                return left, left_sum
            elif (right > 0):
                return right, right_sum
            elif (left_sum+nums[-1]) >= target:
                return len(nums), (left_sum+nums[-1])
            else:
                return 0, (left_sum+nums[-1])

        min_size_sub_array, _ = divide_and_conquer(target, nums)

        return min_size_sub_array

