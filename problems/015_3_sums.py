# Attempt 1: Brute-force method 0(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        three_sums = []
        for idx in range(n):
            for jdx in range(idx+1, n):
                for kdx in range(jdx+1, n):
                    if (nums[idx]+nums[jdx]+nums[kdx] == 0):
                        temp = sorted((nums[idx], nums[jdx], nums[kdx]))
                        if temp not in three_sums:
                            three_sums.append(temp)
        
        return three_sums

