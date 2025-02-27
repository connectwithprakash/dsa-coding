"""
Input: An array of integer
Output: Same array with inplace replacement - do not return anything
Idea: A simple idea would be to iterate over each element and check if its a 0 or not;
if yes have iterate over the array from last until the that initial index
and replace the indexed value with the value before it in the array and skip the 
initial index by 1
else; move along the array, no change
T: O(n^2), S: O(1)
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        idx = 0
        while idx < n:
            # If the number is zero
            if arr[idx] == 0:
                # Move the of the numbers to the right
                for jdx in range(n - 1, idx, -1):
                    arr[jdx] = arr[jdx - 1]
                # Move to the next to the next number
                # because the we replace that next index
                # value by 0
                idx += 2
            # Else just move along next number
            else:
                idx += 1
