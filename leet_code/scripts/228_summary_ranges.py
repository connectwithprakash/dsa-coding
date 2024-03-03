# Simple approach - O(n) solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        idx, jdx = 0, 0
        length = len(nums)
        while jdx < length:
            diff = nums[jdx] - nums[jdx-1]
            if diff > 1:
                if (jdx-idx) == 1:
                    result.append(str(nums[idx]))
                else:
                    result.append(f"{nums[idx]}->{nums[jdx-1]}")
                idx = jdx
            jdx += 1

        if (jdx-1-idx) == 0:
                result.append(str(nums[idx]))
        elif (jdx-idx) > 1:
            result.append(f"{nums[idx]}->{nums[jdx-1]}")                   
        
        return result

