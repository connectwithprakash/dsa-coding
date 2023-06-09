# O(n) space and time complexity.
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    mode_val: int
    freq = 0
    for num in nums:
        if (freq == 0):
            mode_val = num
        if (mode_val == num):
            freq += 1
        else:
            freq -= 1
    return mode_val
 
