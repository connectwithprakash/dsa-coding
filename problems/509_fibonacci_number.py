class Solution:
    def fib(self, n: int) -> int:
        if (n < 2):
            return n
        else:
            n1 = 0
            n2 = 1
            for i in range(n-1):
                n2, n1 = n1 + n2, n2
            
            return n2

