# Attempt 1: Naive O(1) solution
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(n):
            return sum([int(digit)**2 for digit in str(n)])

        past_nums = set()
        while True:
            n = digit_sum(n)
            if n == 1:
                return True
            elif n in past_nums:
                return False
            past_nums.add(n)

