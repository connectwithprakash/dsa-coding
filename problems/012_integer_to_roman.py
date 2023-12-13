# First attempt: Bruteforce solution
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        
        while num != 0:
            if num >= 1000:
                roman += "M"
                num -= 1000
            if 900 <= num < 1000:
                roman += "CM"
                num -= 900
            if 500 <= num < 900:
                roman += "D"
                num -= 500
            if 400 <= num < 500:
                roman += "CD"
                num -= 400
            if 100 <= num < 400:
                roman += "C"
                num -= 100
            if 90 <= num < 100:
                roman += "XC"
                num -= 90
            if 50 <= num < 90:
                roman += "L"
                num -= 50
            if 40 <= num < 50:
                roman += "XL"
                num -= 40
            if 10 <= num < 40:
                roman += "X"
                num -= 10
            if 9 <= num < 10:
                roman += "IX"
                num -= 9
            if 5 <= num < 9:
                roman += "V"
                num -= 5
            if 4 <= num < 5:
                roman += "IV"
                num -= 4
            if 1 <= num < 4:
                roman += "I"
                num -= 1
            
        return roman


