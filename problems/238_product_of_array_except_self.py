## Attempt 1: Using two additional O(n) list
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1]*n
        right_prod = [1]*n

        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]
            right_prod[(n-i)-1] = right_prod[(n-i)] * nums[(n-i)]

        for i in range(n):
            nums[i] = left_prod[i] * right_prod[i]

        return nums


## Attempt 2: Using single additional O(n) list
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)   
        products = [1]*n

        for i in range(1, n):
            products[i] = products[i-1] * nums[i-1]
        
        right_prod = 1
        for i in range(n-2, -1, -1):
            right_prod *= nums[i+1]
            products[i] = products[i] * right_prod
    
        return products

