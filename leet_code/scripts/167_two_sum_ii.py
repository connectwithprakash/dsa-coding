# Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx, jdx = 0, len(numbers)-1
        while idx < jdx:
            summed_val = numbers[idx] + numbers[jdx]
            if summed_val == target:
                return [idx+1, jdx+1]
            elif summed_val > target:
                jdx -= 1
            else:
                idx += 1

