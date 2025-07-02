class Solution:    
    @staticmethod
    def counter(arr):
        arr_dict = {}
        for val in arr:
            if val not in arr_dict:
                arr_dict[val] = 1
            else:
                arr_dict[val] += 1
        return arr_dict
            
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Write your code here
        """
        We have two arrays of equal length. The task is to find 
        if reversal of any number of subarrays in array B can result in 
        array A.
        A: [1, 2, 3, 4, 5, 6, 7, 8]
        B: [1, 4, 3, 2, 5, 7, 6, 8]
        To be reversed: [4, 3, 2], [7, 6]
        
        """
        array_a_count = self.counter(target)
        array_b_count = self.counter(arr)
        for key in array_b_count:
            if (key not in array_a_count):
                return False
            else:
                if (array_a_count[key] != array_b_count[key]):
                    return False
                else:
                    array_a_count.pop(key)
        if len(array_a_count):
            return False
        else:
            return True

