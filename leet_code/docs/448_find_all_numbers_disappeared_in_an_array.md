# Intuition
My first thought was to find a way to identify missing numbers without using extra space beyond the output array. Since we're looking for numbers from 1 to n (array length) that don't appear in the input array, I considered how we could use the array itself to mark the presence of numbers. The idea of placing numbers at their corresponding indices (value-1) emerged as a way to detect what's missing.

# Approach
The solution uses an in-place swapping approach to solve the problem in two phases:

1. First Pass - Organize numbers:
   - Iterate through the array using an index (idx)
   - For each position, try to put the number at its "correct" position (value-1)
   - If the current number equals the index (adjusted for 1-based numbering) or if swapping would place it with a duplicate, move to next index
   - Otherwise, swap the number to its corresponding index
   - This process continues until all numbers are either in their correct positions or can't be moved

2. Second Pass - Identify missing numbers:
   - Scan the array again
   - When an index (adjusted for 1-based numbering) doesn't match its value, that index is a missing number
   - Collect these missing numbers in the output array

For example, with [4,3,2,7,8,2,3,1]:
- After first pass: [1,2,3,4,3,2,7,8]
- Second pass finds 5 and 6 missing as they don't appear at indices 4 and 5

# Complexity
- Time complexity: $$O(n)$$
  - The first while loop runs in O(n) time despite the swaps, as each element can be swapped at most once to its correct position
  - The second while loop is O(n)
  - Total time is still O(n)

- Space complexity: $$O(1)$$
  - Only uses the input array for modifications
  - The output array doesn't count toward space complexity as it's required for the return value
  - No additional data structures are used

# Code
```python3 []
"""
Input: An array of numbers <= length of array
Output: An array with the number that is not present in the original
array i.e. less than or equal to length of array
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
```