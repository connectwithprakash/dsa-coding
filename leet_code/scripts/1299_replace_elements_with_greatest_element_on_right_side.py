"""
Input: An array of numbers
Output: Same array with inplace replacement
Idea: A simple idea would be to loop through all the numbers
and just replace the value with the max of the values to the
right of it. T: O(n^2), S: O(1)
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx in range(len(arr) - 1):
            arr[idx] = max(arr[idx + 1 :])
        arr[-1] = -1

        return arr
