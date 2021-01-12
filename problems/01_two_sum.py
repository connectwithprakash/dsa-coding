class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        count = 0
        temp = nums
        while count<len(nums)-1:
            count += 1
            temp = temp[-1:]+temp[:-1]
            results = [sum(pair) for pair in zip(nums, temp)]
            if target in results:
                y_idx = [index for index, num in enumerate(results) if num == target]
                x_idx = [y_idx[0] - count]
                break
        return x_idx+y_idx
        '''
        for i,f in enumerate(nums):
            temp = nums
            temp[i]=1000
            for j,s in enumerate(temp):
                if f+s == target:
                    return [i, j]
