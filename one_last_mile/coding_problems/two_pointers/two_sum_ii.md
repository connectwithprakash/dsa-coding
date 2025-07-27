# Two Sum II - Input Array Is Sorted

## Problem Statement
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

**Constraint**: You may not use the same element twice. Your solution must use only constant extra space.

## Examples
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

## My Approach
Since the array is **sorted**, I can use the **two-pointer technique** instead of a hashmap:

1. **Start from both ends** - Left pointer at beginning, right pointer at end
2. **Calculate sum** - Add values at both pointers
3. **Move pointers based on sum**:
   - If sum equals target → Found the answer!
   - If sum > target → Move right pointer left (decrease sum)
   - If sum < target → Move left pointer right (increase sum)

**Key insight**: The sorted property allows me to make smart decisions about which pointer to move!

## My Solution
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers)-1
        while head < tail:
            sum_ = numbers[head] + numbers[tail]
            if sum_ == target:
                break
            elif sum_ > target:
                tail -= 1
            else:
                head += 1
        
        return [head+1, tail+1]  # Convert to 1-indexed
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Each element is visited at most once
- **Space Complexity**: O(1) - Only using two pointer variables

**Perfect! Meets both requirements** ✅

## Example Walkthrough
**Input**: `numbers = [2,7,11,15], target = 9`

**Two-pointer process**:
1. `head=0 (2), tail=3 (15)` → sum = 17 > 9 → Move tail left
2. `head=0 (2), tail=2 (11)` → sum = 13 > 9 → Move tail left  
3. `head=0 (2), tail=1 (7)` → sum = 9 = 9 → **Found!**

**Return**: `[0+1, 1+1] = [1, 2]` ✅

## Why This Works (The Magic of Sorted Arrays)

**Why moving pointers is always correct**:
- If `sum > target`: The right pointer points to a value that's too large. Since the array is sorted, any pair including this right value will also be too large. So we can safely eliminate it by moving right pointer left.
- If `sum < target`: The left pointer points to a value that's too small. Since the array is sorted, any pair including this left value will also be too small. So we can safely eliminate it by moving left pointer right.

**We never miss the answer** because we systematically eliminate impossible values!

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Each element is visited at most once
- **Space Complexity**: O(1) - Only using two pointer variables

## What I Learned
- **Sorted array advantage**: Can use two pointers instead of hashmap
- **Space optimization**: O(1) space vs O(n) space of hashmap approach  
- **Pointer movement logic**: Always move the pointer that contributes to the "wrong direction"
- **1-indexed output**: Remember to add 1 to convert from 0-indexed to 1-indexed

## Comparison with Original Two Sum

| Aspect | Two Sum (Unsorted) | Two Sum II (Sorted) |
|--------|-------------------|---------------------|
| **Time** | O(n) | O(n) |
| **Space** | O(n) hashmap | O(1) two pointers |
| **Approach** | Hashmap for complements | Two pointers from ends |
| **Why Different** | No order info | Sorted property enables smart moves |

## Alternative Approaches I Considered

### Binary Search Approach
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        complement = target - numbers[i]
        # Binary search for complement in remaining array
        left, right = i + 1, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1
```
**Complexity**: O(n log n) time - Slower than two pointers

### Hashmap Approach (Like Original Two Sum)
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement] + 1, i + 1]
        seen[num] = i
```
**Complexity**: O(n) time, O(n) space - Works but uses extra space

## Key Insight
My two-pointer approach is **optimal** because:
- **Leverages the sorted property** to make O(1) space possible
- **Each element visited once** ensures O(n) time complexity  
- **Always finds the answer** due to systematic elimination logic
- **Simpler than binary search** and more space-efficient than hashmap

The sorted constraint transforms this from a hashmap problem into an elegant two-pointer problem! 🎯