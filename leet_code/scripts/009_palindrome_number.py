class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp_x = x
            reverse_x = 0
            while(temp_x):
                reverse_x = reverse_x * 10 + temp_x % 10
                temp_x = temp_x // 10
            return (x == reverse_x)

