"""
Input: An array of numbers
Output: Same array but all the 0s to the right
Idea: A simple approach would be to use two pointer, one read pointer 
that will read the indexed value and the write pointer will write the
indexed value, the logic is like this; the read pointer will read each
number and compare it with the write pointer, the write pointer will 
hold the index to store the the non-zero value, we need to be careful 
about the case where both the pointer have the same value then we just 
move the read pointer to the right. T: O(n), S: O(1)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            read_ptr, write_ptr = 1, 0
            # Find the first position of zero that needs to be
            # moved
            while write_ptr < len(nums):
                if nums[write_ptr] == 0:
                    break
                else:
                    write_ptr += 1
            read_ptr = write_ptr + 1
            # Do the replacement
            while read_ptr < len(nums):
                if nums[read_ptr] != 0:
                    nums[write_ptr] = nums[read_ptr]
                    nums[read_ptr] = 0
                    write_ptr += 1
                read_ptr += 1
