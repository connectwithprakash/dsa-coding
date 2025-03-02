"""
Input: Array of numbers
Output: Same array with even numbers first followed by the odd
numbers and the order of numbers doesn't matter
Idea: A simple idea would be to loop through each numbers and just
keep on moving the odd numbers to the right. T: O(n), S:O(1)
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            jdx = 0
            # Find the first odd number
            while jdx < len(nums):
                if nums[jdx] % 2:
                    break
                jdx += 1
            # Move the even numbers to the left
            idx = jdx + 1
            while idx < len(nums):
                if not nums[idx] % 2:
                    temp = nums[jdx]
                    nums[jdx] = nums[idx]
                    nums[idx] = temp
                    jdx += 1
                idx += 1

        return nums
