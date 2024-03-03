# O(n^2) time complexity

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = 0
        temp = nums
        total = len(nums)
        while count<total-1:
            count += 1
            temp = temp[-1:]+temp[:-1]
            results = [sum(pair) for pair in zip(nums, temp)]
            if target in results:
                for index, num in enumerate(results):
                    if num == target:
                        y_idx = index
                        break
                x_idx = (y_idx+total-count)%total
                #x_idx = y_idx - count
                break
        return [x_idx,y_idx]


# Less than O(n^2) solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index in range(len(nums)):
            if nums[index] in hash_map:
                return [hash_map[nums[index]], index]
            else:
                hash_map[(target - nums[index])] = index

