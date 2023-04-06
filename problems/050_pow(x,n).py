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

# Attempt 2: With memoization
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        dp = {
            0: 1,
            1: x
        }

        def pow(n):
            if n in dp:
                return dp[n]
            temp = x
            i = 2
            while (i <= n):
                print("i: ", i, " temp: ", temp)
                temp *= temp
                dp[i] = temp
                i *= 2
            return temp * pow(n - (i//2))
        return pow(n)


# Attempt 3: Improved solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n < 0):
            n = -n
            x = 1/x
        
        def helper(n):
            if (n == 0):
                return 1
            elif (n == 1):
                return x
            else:
                pow = helper(n//2)
                pow *= pow
                if (n % 2) == 1:
                    pow *= x
                return pow
        return helper(n)

