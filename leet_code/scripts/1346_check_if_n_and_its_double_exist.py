"""
Input: An array of numnbers
Output: To check if there is an indices i and j such and they are not
equal and ith indexed element is double of the jth element or vice versa
because the indexes coulbe be reversed
Idea: Simplementation approach would be to take one number and compare
it with the others. T: O(n^2), S: O(1)

Second approach would be to have a set where we can look up already seen
numbers that we can use to check if the half or double exists. T: O(n), O()
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # # Simple approach
        # n = len(arr)
        # for idx in range(n-1):
        #     for jdx in range(idx+1, n):
        #         if (arr[idx] == 2*arr[jdx]) or (arr[jdx] == 2*arr[idx]):
        #             return True

        # return False

        # Faster approach
        seen_nums = set()
        for num in arr:
            if num * 2 in seen_nums:
                return True
            elif (num % 2 == 0) and ((num // 2) in seen_nums):
                return True
            seen_nums.add(num)

        return False
