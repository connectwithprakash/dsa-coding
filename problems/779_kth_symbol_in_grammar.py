class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n=1: 0
        # n=2: 01
        # n=3: 0110
        # n=4: 01101001
        # n=5: 0110100110010110
        dp = [0, 1, 1, 0, 1]
        def helper(k):
            if (k < 6):
                return dp[k-1]
            else:
                return 1 if helper(k//2) == 0 else 0

        return helper(k)
 
