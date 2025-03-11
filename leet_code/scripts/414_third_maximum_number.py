"""
Input: An array of numbers
Output: the third maximum number if exists else the maximum
Idea: A simple approach would be to create is have a list
of size 3, and we traverse the nums and if we see maximum than
the heap we remove the min and put current num to the list
We return the min of that list. T: O(n*k), S: O(1)

Another approach would be to have a variable that stores the three max values.
At each iteration we check if the new number gets the place of either first
second or third maximum place and replace old value with the new one and then
return the third value. T: O(n), S: O(1)
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        max_nums = [float("-inf")] * 3
        for num in nums:
            if (num == max_nums[0]) or (num == max_nums[1]) or (num == max_nums[2]):
                continue
            elif num > max_nums[0]:
                max_nums = [num, max_nums[0], max_nums[1]]
            elif num > max_nums[1]:
                max_nums[1:] = [num, max_nums[1]]
            elif num > max_nums[2]:
                max_nums[2] = num

        if max_nums[2] != float("-inf"):
            return max_nums[2]
        else:
            return max_nums[0]
