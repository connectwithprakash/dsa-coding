# Naive solution - needs refactoring
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums[-1] = 1
        
        def helper(j, step):
            # Handles base case
            if (j == 0):
                return True
            # Handles lookbask index
            elif ((j-step) < 0):
                return False
            # If the step that needs to be taken is greater than possible step
            if step > nums[j-step]:
                return helper(j, step+1)
            else:
                return helper(j-step, 1)

        return helper(n-1, 1)

