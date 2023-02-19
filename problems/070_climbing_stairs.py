class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if (n==0):
            return 1
        elif (n < 0):
            return 0
        else:
            if (n-1) not in self.dp:
                self.dp[n-1] = self.climbStairs(n-1)
            if (n-2) not in self.dp:
                self.dp[n-2] = self.climbStairs(n-2)
            return  self.dp[n-1] + self.dp[n-2]

