# Linear time solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for idx in reversed(range(1, n)):
            if (n-idx) > nums[idx-1]:
                continue
            else:
                n = idx

        return (n < 2)

