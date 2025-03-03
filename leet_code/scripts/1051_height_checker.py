"""
Input: An array of heights
Output: Count of the errors in the height arrangement
Idea: A simple approach would be to sort the array
into another array and find the numebr of mismatch. T: O(n), S: O(n)

Complex idea: For a increasing array, the number at i-1th is smaller
and i+1th is greater than ith number. So, a simple idea would 
be to just check the surrounding numbers and if the condition
does not satisfy, we have an error. Simply counting those 
numbers should do. T: O(n), S: O(1) - Not implemented completely
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        error_count = 0
        expected_heights = sorted(heights)
        print(expected_heights)
        # Cound the errors
        for idx in range(len(heights)):
            if heights[idx] != expected_heights[idx]:
                error_count += 1

        # Sort the array
        #         for idx in range(len(heights)):
        #             # Check if the left is smaller than the current
        #             # idx is not the end
        #             if idx+1 <len(heights):
        #                 if heights[idx] < heights[idx+1]:
        #                     right_check = True
        #                 else:
        #                     right_check = False
        #             else:
        #                 right_check = True
        #             # Check if the right is greater than the current
        #             # idx is not at the start of the array
        #             if idx-1 > 0:
        #                 if heights[idx] < heights[idx-1]:
        #                     left_check = True
        #                 else:
        #                     left_check = False
        #             # idx is at the start of the array
        #             else:
        #                 left_check = True

        #             if left_check and right_check:
        #                 error_count += 1

        return error_count
