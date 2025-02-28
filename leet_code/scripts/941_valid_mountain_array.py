"""
Input: An array of numbers either forming a mountain or not
Output: Return a boolean saying if the mountain 
Idea: A mountain should comprise of strict positive slope and
then a strict neagative slope on the right and left side of the
peak. Also, it needs to have both the halves.

Simple apporach would be to to find the peak of the mountain
Divide the array into two halves. First check for positive
slope at each neighboring numbers and then check of negative
slope with other half. T: O(n), S: O(1)


"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # First condition
        if len(arr) < 3:
            return False
        # Find the peak
        peak_idx = next((idx for idx in range(len(arr)) if arr[idx] == max(arr)))
        # Check if we have two halves or not by checking their length
        if not len(arr[:peak_idx]) or not len(arr[peak_idx + 1 :]):
            return False

        # Check if the array is a valid mountation
        # Verify that the left half has increasing slope
        for idx in range(1, peak_idx + 1):
            if (arr[idx] - arr[idx - 1]) <= 0:
                return False
        # Verify that the right half has decreasing slope
        for jdx in range(peak_idx, len(arr) - 1):
            if (arr[jdx] - arr[jdx + 1]) <= 0:
                return False

        return True
