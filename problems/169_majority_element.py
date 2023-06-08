class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {num: 0 for num in nums}
        max_freq_val = nums[0]
        max_freq = 1
        for num in nums:
            counts[num] += 1
            if counts[num] > max_freq:
                max_freq = counts[num]
                max_freq_val = num

        return max_freq_val

