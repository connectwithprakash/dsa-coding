class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,0,4,5,6,7]
        # for (k=3)
        # [5,6,7,0,4,1,2,3]
        # Next for k=3
        # [5,6,7,1,4,0,2,3]
        # [5,6,7,1,2,0,4,3]
        # [5,6,7,1,2,3,4,0]
        # next for k=1
        # [5,6,7,1,2,3,0,4]
        # offset = 0
        # n = len(nums)
        # while True:
        #     k = k % (n - offset) # (n-offset) is number of items rotated
        #     if k == 0:
        #         break
        #     for i in range(n-k, n):
        #         swap_i = ((i + k) % n) + offset # swap_i is the new position
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
        reverse(nums, 0, n - 1)
        # Reverse left half
        reverse(nums, 0, k - 1)
        # Reverse right half
        reverse(nums, k, n - 1)
