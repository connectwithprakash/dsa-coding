"""
Input: Array of numbers
Output: Array of numbers (digits) after adding 1 to the 
number represented by the digits
Idea: A simple approach would be to just do the addition 
to the numbers from right to left. If there is carry at 
the end, we can just append the array with a 0 at the end 
and set the most significant digit to 1. Coz this is the 
case of numbers that are all digits 9s. T: O(n), O: O(1)
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        idx = len(digits) - 1
        # Run addition
        while idx >= 0:
            if carry:
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += carry
                    carry = 0
            else:
                break
            idx -= 1
        
        # If most significant digit is a 9
        if carry:
            digits.append(0)
            digits[0] = 1
            
        return digits
