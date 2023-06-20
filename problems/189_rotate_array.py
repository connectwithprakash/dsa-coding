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
        rem_n = len(nums)
        n = len(nums)
        while True:
            k = k % rem_n
            if k == 0:
                break
            for i in range(n-k, n):
                new_i = ((i+k)%n)+offset
                nums[new_i], nums[i] = nums[i], nums[new_i]
            rem_n = rem_n-k
            offset += k

