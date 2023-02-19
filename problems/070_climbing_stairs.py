class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if (n < 3):
            return n
        else:
            minus1 = 2
            minus2 = 1
        for i in range(3, n+1):
            minus1, minus2 = minus1 + minus2, minus1

        return minus1

