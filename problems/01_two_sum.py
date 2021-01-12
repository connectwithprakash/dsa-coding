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
        '''
        for i,f in enumerate(nums):
            temp = nums
            temp[i] = 10000
            for j,s in enumerate(temp):
                if f+s == target:
                    return [i, j]
        
        '''
