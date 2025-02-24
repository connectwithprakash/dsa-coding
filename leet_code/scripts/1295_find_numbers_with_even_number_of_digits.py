"""
Input: An array of numbers 
Output: The count of numbers with even number of digits
Idea: A simple idea would be go through all the numbers, convert into string and see if the length is even or odd and count the even lengthed numbers. The solution would be compute inefficient.
Time complexity -> n*k where n is the count of numbers and k is the maximum number of digits
Space complexity -> k
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # return sum((True for num in nums if not len(str(num)) % 2)) -> Fastest

        """
        Let's try to atleast decrease the space complexity to constant
        What we could do is create a variable to keep track of the count of numbers with even number of digits.
        And create a function that would do a repeated division to find out the number of times the division occured by 10
        to get the count of the digits present in the number
        """

        def number_of_digits(num):
            # Recursive approach is slow
            # if not num:
            #     return 0
            # return number_of_digits(num // 10) + 1

            # Better than above
            digits_count = 0
            while num:
                num = num // 10
                digits_count += 1
            return digits_count

        # Do a bit wise and to see if we have even or odd number of digits for each number and sum them together
        return sum(not number_of_digits(num) & 1 for num in nums)
