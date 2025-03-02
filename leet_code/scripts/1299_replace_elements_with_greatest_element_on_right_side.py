"""
Input: An array of numbers
Output: Same array with inplace replacement
Idea: A simple idea would be to loop through all the numbers
and just replace the value with the max of the values to the
right of it. T: O(n^2), S: O(1)

Another approach would be to move around the numbers with idx
and find the max of rest of the array, and then move idx until
this max value and then repeat again. T: O(n^2) - O(n), S: O(1)

Another even faster approach would be have keep track of the
maximum value and at each time we find the maximum value we then
move start finding the max value again

Let's try again another approach would be to look at the output.
The output will be a decending numbered array. So, if we go from
last we just need to keep track that the cell to the right is
is greater than the current cell because if the right is greater 
than the current cell then that value is the maximum to the right
of the rest of the array. T: O(n), S: O(1)
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for idx in range(len(arr)-1):
        #     arr[idx] = max(arr[idx+1:])
        # arr[-1] = -1

        # # A little faster approach
        # max_val = arr[0]
        # for idx in range(len(arr)-1):
        #     if arr[idx] == max_val:
        #         max_val = max(arr[idx+1:])
        #     arr[idx] = max_val
        # arr[-1] = -1

        # Yet another approach
        max_val = -1
        for idx in range(len(arr) - 1, -1, -1):
            if arr[idx] > max_val:
                # Swap variables
                temp_val = arr[idx]
                arr[idx] = max_val
                max_val = temp_val
            else:
                arr[idx] = max_val

        return arr
