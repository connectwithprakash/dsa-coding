"""
Input: An array of numbers 
Output: The count of numbers with even number of digits
Idea: A simple idea would be go through all the numbers, convert into string and see if the length is even or odd and count the even lengthed numbers. The solution would be compute inefficient.
Time complexity -> n*k where n is the count of numbers and k is the maximum number of digits
Space complexity -> k
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((True for num in nums if not len(str(num)) % 2))
