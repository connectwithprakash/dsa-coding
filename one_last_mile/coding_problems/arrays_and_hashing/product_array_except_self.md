# Product of Array Except Self

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Constraints**: 
- You must write an algorithm that runs in O(n) time
- You cannot use the division operation

## Examples
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2*3*4 = 24
- answer[1] = 1*3*4 = 12
- answer[2] = 1*2*4 = 8
- answer[3] = 1*2*3 = 6

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## My Approach
I need to find the product of all elements except the current one. My strategy uses **prefix and suffix products**:

1. **Left products**: For each index, store the product of all elements to its left
2. **Right products**: For each index, store the product of all elements to its right  
3. **Final result**: Multiply left[i] × right[i] to get the product except nums[i]

**Key insight**: For index i, the result is (product of elements 0 to i-1) × (product of elements i+1 to n-1)

## My Solution (Corrected)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Build left products array
        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Build right products array  
        right_products = [1] * n
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        # Combine left and right products
        result = []
        for i in range(n):
            result.append(left_products[i] * right_products[i])
        
        return result
```

## Example Walkthrough
**Input**: `nums = [1, 2, 3, 4]`

**Step 1 - Left products**:
- `left_products[0] = 1` (no elements to the left)
- `left_products[1] = 1` (product of [1] = 1)
- `left_products[2] = 1 * 2 = 2` (product of [1,2] = 2)
- `left_products[3] = 2 * 3 = 6` (product of [1,2,3] = 6)
- Result: `[1, 1, 2, 6]`

**Step 2 - Right products**:
- `right_products[3] = 1` (no elements to the right)
- `right_products[2] = 4` (product of [4] = 4)
- `right_products[1] = 4 * 3 = 12` (product of [3,4] = 12)  
- `right_products[0] = 12 * 2 = 24` (product of [2,3,4] = 24)
- Result: `[24, 12, 4, 1]`

**Step 3 - Final result**:
- `result[0] = left_products[0] * right_products[0] = 1 * 24 = 24`
- `result[1] = left_products[1] * right_products[1] = 1 * 12 = 12`
- `result[2] = left_products[2] * right_products[2] = 2 * 4 = 8`
- `result[3] = left_products[3] * right_products[3] = 6 * 1 = 6`
- Final: `[24, 12, 8, 6]` ✅

## Space-Optimized Version (O(1) extra space)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # First pass: store left products in result array
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # Second pass: multiply by right products on the fly
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * right_product
            right_product *= nums[i]
        
        return result
```

## Complexity Analysis
- **Time Complexity**: O(n) - Three passes through the array
- **Space Complexity**: O(1) extra space (not counting output array)

## What I Learned
- **Prefix/Suffix pattern**: Breaking down the problem into left and right products
- **Space optimization**: Using the output array to store intermediate results
- **Boundary handling**: Elements at edges only have products from one side
- **Why division is avoided**: This approach works even with zeros in the array

## My Original Approach (For Reference)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # Create multiplication (cumulative from left to right)
        right_dir_mul = nums.copy()
        left_dir_mul = nums.copy()
        n = len(nums)
        
        for idx in range(n):
            if idx == 0:
                pass
                # -> [1, 2, 4, 6]
                # <- [1, 2, 4, 6]
            else:
                rev_idx = (n-idx-1)
                # rev_idx = 2
                right_dir_mul[idx] = right_dir_mul[idx-1] * right_dir_mul[idx]
                left_dir_mul[rev_idx] = left_dir_mul[rev_idx]*left_dir_mul[rev_idx+1]
                # idx = 1 | -> [1, 2, 4, 6] <-[1, 2, 24, 6]
                # idx = 3 | -> [1, 2, 8, 48] | <- [48, 48, 24, 6]

        # Take the right and left of that index and multiply left and right to get the array products except that
        # Except for the boundary condition where we just take the non boundary item
        res = [0]*n
        # [0, 0, 0 ,0]
        for idx in range(n):
            if idx == 0:
                idx_mul = left_dir_mul[idx+1]
                # 48
            elif idx == (n-1):
                idx_mul = right_dir_mul[idx-1]
                # 8
            else:
                idx_mul = right_dir_mul[idx-1]*left_dir_mul[idx+1]
                # 1*48
                # 2*24
            res[idx] = idx_mul
            # [48, 48, 24, 8]
        return res
```

## Issues in My Original Approach
1. **Cumulative multiplication error**: I was modifying the copied arrays during iteration, which corrupted the products
2. **Index calculation**: The reverse index logic (`rev_idx = n-idx-1`) was overcomplicated
3. **Boundary conditions**: Handling first/last elements separately made the code more complex than needed
4. **Logic confusion**: Trying to build both left and right products in the same loop led to incorrect calculations

## Key Insight
The prefix/suffix product pattern is fundamental in array problems. Instead of thinking about "products except self," I think about:
- "What's the product of everything to my left?"
- "What's the product of everything to my right?"
- Multiply these two together!

This pattern appears in many other problems and is worth mastering.