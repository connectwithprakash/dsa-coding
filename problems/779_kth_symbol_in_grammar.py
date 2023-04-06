class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n=1: 0
        # n=2: 01
        # n=3: 0110
        # n=4: 01101001
        # n=5: 0110100110010110
        if (k == 1):
            return 0
        else:
            max_cap = 2**(n-1)
            if (k < max_cap):
                return self.kthGrammar(n-1, k)
            elif (k == max_cap):
                return 1^self.kthGrammar(n-1, k//2)
            else:
                return 1^self.kthGrammar(n, k - max_cap)            

