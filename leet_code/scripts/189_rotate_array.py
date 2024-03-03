## Attempt 1: Pythonic solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Naive pythonic way
        k = (k % len(nums))
        nums[:] = nums[-k:] + nums[:-k]


## Approach 2: Divide the array into from pivot idx and reverse each and then reverse combined.


## Attempt 2: My solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        offset = 0
        n = len(nums)
        while True:
            k = k % (n - offset)
            if k == 0:
                break
            for i in range(n-k, n):
                swap_i = ((i + k) % n) + offset
                nums[swap_i], nums[i] = nums[i], nums[swap_i]
            offset += k

