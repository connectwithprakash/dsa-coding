class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # offset = 0
        # n = len(nums)
        # while True:
        #     k = k % (n - offset)
        #     if k == 0:
        #         break
        #     for i in range(n-k, n):
        #         swap_i = ((i + k) % n) + offset
        #         nums[swap_i], nums[i] = nums[i], nums[swap_i]
        #         print(nums, k)
            # offset += k

        # Another easier to understand solution
        n = len(nums)
        k = k % n
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Reverse full array
        reverse(nums, 0, n-1)
        # Reverse left half
        reverse(nums, 0, k-1)
        # Reverse right half
        reverse(nums, k, n-1)

