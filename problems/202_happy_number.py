# Attempt 1: Naive O(n^2) solution
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(n):
            return sum([int(digit)**2 for digit in str(n)])

        dig_sum = n
        digits = []
        while True:
            dig_sum = digit_sum(dig_sum)
            if dig_sum == 1:
                return True
            elif dig_sum in digits:
                return False
            digits.append(dig_sum)

