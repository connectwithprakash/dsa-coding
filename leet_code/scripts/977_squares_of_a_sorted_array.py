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
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Poor implementation
        pivot_index = 0
        # finding the pivot index using slope formula, T: O(n)
        for idx in range(len(nums)):
            # Finding pivot point
            if nums[idx] > 0:
                break
        pivot_index = idx

        # Square the numbers
        nums = [num**2 for num in nums]
        print(pivot_index)

        # Merge the two section of the array, T: O(n)
        if pivot_index:
            idx = pivot_index - 1
            jdx = pivot_index
            squared_nums = []  # S: O(n)
            while (idx > -1) and (jdx < len(nums)):
                print("in loop")
                if nums[idx] > nums[jdx]:
                    squared_nums.append(nums[jdx])
                    jdx += 1
                else:
                    squared_nums.append(nums[idx])
                    idx -= 1

            if idx > -1:
                squared_nums.extend(nums[idx::-1])
            if jdx < len(nums):
                squared_nums.extend(nums[jdx::])
        else:
            squared_nums = nums

        return squared_nums
