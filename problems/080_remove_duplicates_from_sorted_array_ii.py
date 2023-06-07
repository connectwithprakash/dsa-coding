class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 2
        for num in nums[idx:]:
            if (num != nums[idx-1]) or (num != nums[idx-2]):
                nums[idx] = num
                idx += 1        
        return idx

