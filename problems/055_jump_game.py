## DP solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        # Populating DP table
        for i in range(n):
            idx_val = nums[i]
            for k in range(idx_val+1):
                j = i+k
                if j < n:
                    dp[i][j] = k
                else:
                    break
        # Backtracking result
        def helper(j):
            if j == 0:
                return True

            for i in range(j):
                if dp[i][j] > 0:
                    val = dp[i][j]
                    return helper(j-val)
                else:
                    continue
                    
            return False

        return helper(n-1)

