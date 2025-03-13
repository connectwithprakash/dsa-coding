"""
Input: An array of numbers <= length of array
Output: An array with the number that is not present in the original
array i.e. less than or equal to length of an array
Idea: A simple approach would be to have an idx that swaps the element
with the element at position given by the value at idx if the current 
value is not same as the idx. If the value is same as the idx then we
move the idx to next value. We also move the idx ahead in the situation
where the value at idx and the value at jdx (=value at idx) are equal.
So in a single pass, we will have all the numbers in their respective
idx place. In another pass we will just compare the idx == value at idx,
 if not we add this idx to the output. T: O(n), S: O(1)

> Swapping values to right index
idx=1, [4, 3, 2, 7, 8, 2, 3, 1]
1, [7, 3, 2, 4, 8, 2, 3, 1]
1, [3, 3, 2, 4, 8, 2, 7, 1]
1, [2, 3, 3, 4, 8, 2, 7, 1]
1, [3, 2, 3, 4, 8, 2, 7, 1]
2, [3, 2, 3, 4, 8, 2, 7, 1]
3, [3, 2, 3, 4, 8, 2, 7, 1]
4, [3, 2, 3, 4, 8, 2, 7, 1]
5, [3, 2, 3, 4, 8, 2, 7, 1]
5, [3, 2, 3, 4, 1, 2, 7, 8]
5, [1, 2, 3, 4, 3, 2, 7, 8]
6, [1, 2, 3, 4, 3, 2, 7, 8]
7, [1, 2, 3, 4, 3, 2, 7, 8]
8, [1, 2, 3, 4, 3, 2, 7, 8]
> Extract the values that are not equal to the index
[5, 6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 1
        # Swap values to its right index
        while idx <= len(nums):
            jdx = nums[idx-1]
            if (idx == nums[idx-1]) or (nums[idx-1] == nums[jdx-1]):
                idx += 1
            else:
                nums[idx-1], nums[jdx-1] = nums[jdx-1], nums[idx-1]
        # Check which value is not present
        idx = 1
        missing_nums = []
        while idx <= len(nums):
            if idx != nums[idx-1]:
                missing_nums.append(idx)
            idx += 1
        
        return missing_nums
