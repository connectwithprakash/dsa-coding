# O(n) space and time complexity.

# The idea is to find the element that is more frequent progressively.
# A thing to remember is that the code scans element and increases the count
# and decreases if the character is not same and we just want the count to be
# greater than 0. Having count 0 means that no element is occurs more than n/2


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
 
