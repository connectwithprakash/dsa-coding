"""
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Comments: The input and output size is same and the each element in the output is the sum of all the numbers upto the index number of the array nums
Idea: We can do a inplace or no inplace sum assignment, inplace assignment has O(1) space complexity, and no inplace has O(n) space complexity because we will be creating a new array for the output.
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums
        for index in range(len(running_sum)):
            if index == 0:
                continue
            else:
                running_sum[index] = running_sum[index - 1] + running_sum[index]

        return running_sum
