"""
Input: An array of numbers
Output: the third maximum number if exists else the maximum
Idea: A simple approach would be to create is have a list
of size 3, and we traverse the nums and if we see maximum than
the heap we remove the min and put current num to the list
We return the min of that list. T: O(n*k), S: O(1)
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = set()
        for idx in range(len(nums)):
            if len(max_nums) == 3:
                break
            else:
                max_nums.add(nums[idx])
        if len(max_nums) < 3:
            return max(max_nums)
        else:
            start_idx = idx
            while start_idx < len(nums):  # O(n)
                if nums[start_idx] not in max_nums and nums[start_idx] > min(max_nums):  # O(k)
                    max_nums.remove(min(max_nums))  # O(2*k)
                    max_nums.add(nums[start_idx])  # O(k)
                start_idx += 1
            return min(max_nums)
