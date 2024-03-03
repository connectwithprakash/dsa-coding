class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        head, tail, steps = 0, 0, 0
        
        for idx in range(n):
            if tail > n:
                break
            # See whether we can reach current index from previous step
            if idx > tail:
                tail = head
                steps += 1
            # Tracks where can we reach if we take an another step
            head = max(head, idx+nums[idx])

        return steps

