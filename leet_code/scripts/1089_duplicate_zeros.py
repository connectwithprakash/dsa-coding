"""
Input: An array of integer
Output: Same array with inplace replacement - do not return anything
Idea: A simple idea would be to iterate over each element and check if its a 0 or not;
if yes have iterate over the array from last until the that initial index
and replace the indexed value with the value before it in the array and skip the 
initial index by 1
else; move along the array, no change
T: O(n^2), S: O(1)

Second Attempt:
Let's find out the number of zeros there are that would be duplicated and then consider 
this being the position from last upto which the numbers can be replaced/deleted
So, now we can start placing the numbers from packward and repeat 0 when found one
T: O(n), S: O(1)
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # n = len(arr)
        # idx = 0
        # while idx < n:
        #     # If the number is zero
        #     if arr[idx] == 0:
        #         # Move the of the numbers to the right
        #         for jdx in range(n-1, idx, -1):
        #             arr[jdx] = arr[jdx-1]
        #         # Move to the next to the next number
        #         # because the we replace that next index
        #         # value by 0
        #         idx += 2
        #     # Else just move along next number
        #     else:
        #         idx += 1

        # 2nd attempt - cool approach -
        n = len(arr)
        # Find the number of dups needed
        dup_count = 0
        idx = 0
        while idx + dup_count < n:
            if arr[idx] == 0:
                # Edge case where a zero can not be duplicated
                #  because of the size of the array
                if (idx + dup_count + 1) == n:
                    arr[n - 1] = 0
                    break
                dup_count += 1
            idx += 1
        # Fix the index to the position from where we want to
        # check if the number is zero, which means repeatation
        idx -= 1

        # Repeat the zeros
        while idx >= 0:
            if arr[idx] == 0:
                arr[idx + dup_count] = 0
                dup_count -= 1
            arr[idx + dup_count] = arr[idx]
            idx -= 1
