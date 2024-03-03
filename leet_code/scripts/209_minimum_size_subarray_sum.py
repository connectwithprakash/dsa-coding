# Attempt 1: Brute-force O(n^3) solution
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

# Brute-force O(n^2) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = 0
        for idx in range(n):
            window_sum = 0
            for jdx in range(idx, n):
                window_sum += nums[jdx]
                if window_sum >= target:
                    if min_len != 0:
                        min_len = min(min_len, jdx-idx+1)
                    else:
                        min_len = jdx-idx+1

        return min_len


# Attempt 4: O(n) efficient solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        idx, jdx = 0, 0 # Pointers defining the window
        win_sum = 0
        min_len = n+1
        while idx <= jdx and jdx < n:
            win_sum += nums[jdx] # Increamentally accumulate the sum
            if win_sum >= target: # We have found the sum for idx
                min_len = min(min_len, jdx-idx+1)
                # Now we can look for (idx+1)th position for the window
                # But also jdx position might itself contribute to >= target value
                # even when idx position is not there in the sum
                # So, we remove that as well from the summed value and check again
                win_sum -= (nums[idx] + nums[jdx])
                idx += 1
            else: # We keep on increasing the window size for ith position
                jdx += 1

        if min_len < (n+1):
            return min_len
        else:
            return 0

