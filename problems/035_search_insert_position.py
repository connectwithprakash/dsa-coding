# Search inser position using binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                break
            elif (target < nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        
        if (target > nums[mid]):
            return mid + 1
        else:
            return mid

