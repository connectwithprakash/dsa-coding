"""
Input: An array of numbers
Output: Index of the number in the array that is at least 2x
 to the rest of the numbers, if not found return -1
Idea: A simple approach would be to first find the largest 
number and then in another loop see if other numbers are 
lesser than half of the max number. T: O(n), O:(1)
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_half_val = max_val/2.0
        # Check if the number is less than half of the max value
        idx = 0
        while idx < len(nums):
            if nums[idx] <= max_half_val:
                pass
            elif nums[idx] == max_val:
                max_idx = idx
            else:
                return -1
            idx += 1
        return max_idx
