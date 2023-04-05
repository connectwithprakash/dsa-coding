# First Attempt: Without memoization
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        def pow(n):
            if (n == 0):
                return 1
            elif (n == 1):
                return x
            temp = x
            i = 2
            while (i <= n):
                print("i: ", i, " temp: ", temp)
                temp *= temp
                i *= 2
            return temp * pow(n - (i//2))
        return pow(n)

