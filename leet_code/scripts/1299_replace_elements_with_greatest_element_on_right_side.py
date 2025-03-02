"""
Input: An array of numbers
Output: Same array with inplace replacement
Idea: A simple idea would be to loop through all the numbers
and just replace the value with the max of the values to the
right of it. T: O(n^2), S: O(1)

Another approach would be to move around the numbers with idx
and find the max of rest of the array, and then move idx until
this max value and then repeat again. T: O(n^2), S: O(1)
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for idx in range(len(arr)-1):
        #     arr[idx] = max(arr[idx+1:])
        # arr[-1] = -1

        # A little faster approach
        max_val = arr[0]
        for idx in range(len(arr) - 1):
            if arr[idx] == max_val:
                max_val = max(arr[idx + 1 :])
            arr[idx] = max_val
        arr[-1] = -1

        return arr
