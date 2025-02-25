"""
Input: Array of numbers in an increasing order
Output: Array of the squares of each number in increasing order
Idea: A simple idea would be to sqare the numbers and some how sort the numbers 
because the squares of negative numbers are not not sorted. So, our approach could be
- Go through each numbers
    - Set the pivot point as the point where negative becomes positive
    - Square the numbers
- Go throught the numbers again but with two pointers
    - first pointer is at the one step behind pivot point and decreases 
    - second pointer is at the pivot point and increases
    - Now, we do a merge part of the sort.

Complexity:
- Time complexity should be O(n)
- Space complexity would be O(n)

Original solution is equally good.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # Let's do the same thing with clean code
        # # Find the pivot index
        # pivot_idx = next((idx for idx, num in enumerate(nums) if num >= 0), len(nums)-1)
        # # Square each number
        # nums = [num**2 for num in nums]
        # # Now, Create an array with two pointers
        # # Merge the two section of the array, T: O(n)
        # def merge_sorted_arrays(first: List[int], second: List[int]):
        #     merged = []
        #     idx = jdx = 0
        #     while idx < len(first) and jdx < len(second):
        #         if first[idx] <= second[jdx]:
        #             merged.append(first[idx])
        #             idx += 1
        #         else:
        #             merged.append(second[jdx])
        #             jdx += 1
        #     merged.extend(first[idx:])
        #     merged.extend(second[jdx:])
        #     return merged

        # return merge_sorted_arrays(nums[:pivot_idx][::-1], nums[pivot_idx:])

        # Second attempt | Simiar solution
        idx, jdx = 0, len(nums) - 1
        sorted_squared_nums = []
        while idx <= jdx:
            if abs(nums[idx]) > abs(nums[jdx]):
                sorted_squared_nums.append(nums[idx] ** 2)
                idx += 1
            else:
                sorted_squared_nums.append(nums[jdx] ** 2)
                jdx -= 1

        return sorted_squared_nums[::-1]
