# Attempt 1: Naive O(nlongn) solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        nums.sort()
        length = 1
        idx = 0
        repeat = 0
        for jdx in range(1, len(nums)):
            diff = (nums[jdx] - nums[jdx-1])
            if diff > 1:
                idx = jdx
                repeat = 0
            elif diff == 0:
                repeat += 1
            else:
                curr_len = (jdx-idx-repeat+1)
                if curr_len > length:
                    length = curr_len            

        return length


# Attempt 2: Optimized O(n) solution using set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This is a O(n) solution because we only visit each number twice
        # Convert into set
        nums_s = set(nums)
        length = 0
        for num in nums:
            if (num-1) in nums_s:
                continue
            else:
                surplus = 1
                # Increase the surplus when consecutive num is found
                while (num+surplus) in nums_s:
                    surplus += 1
                if (surplus > length):
                    length = surplus
        
        return length

