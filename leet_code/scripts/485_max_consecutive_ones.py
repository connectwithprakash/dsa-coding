"""
Input: An array/list of numbers
Output: Find the total length of the longest sequence of 1s
Idea: A simple idea would be to iterate through the array, keep a pointer seq_idx tracks the head 1 of the sequence, and at the end of the sequence, set the max length variable
So, for the example 1
seq_idx at 0, idx at 0
if idx has 1 -> head at idx
at idx 0 we have 1 -> seq_idx at 0, idx at 1 (+1)
at idx 1 we have 1 -> head at 0, idx at 2 (+1)
at idx 2 we have 0 != 1 -> max_num_consecutive_ones = max(max_num_consecutive_ones, idx - seq_idx), seq_idx at idx, idx at 3 (+1),
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num_consecutive_ones = 0
        seq_idx = 0
        # Looping through all the cells
        for idx in range(len(nums)):
            if not nums[idx]:
                max_num_consecutive_ones = max(max_num_consecutive_ones, (idx - seq_idx))
                seq_idx = idx + 1

        # Check for last ones sequence
        max_num_consecutive_ones = max(max_num_consecutive_ones, (idx - seq_idx) + 1)

        return max_num_consecutive_ones
