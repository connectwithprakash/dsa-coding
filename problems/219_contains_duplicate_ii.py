# Attempt 1: Naive approach O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for idx in range(n):
            for jdx in range(idx+1, n):
                if (nums[idx] == nums[jdx]) and ((jdx - idx) <= k):
                    return True
        return False


# Attempt 2: Optimized O(n^2) using hashmap
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for idx, num in enumerate(nums):
            if num in hashmap:
                hashmap[num].append(idx)
            else:
                hashmap[num] = [idx]

        found = False
        for key in hashmap:
            values = hashmap[key]
            if len(values) == 1:
                continue
            for i in range(len(values)-1):
                if (values[i+1] - values[i]) <= k:
                    found = True
                    break
            if found:
                break

        return found

