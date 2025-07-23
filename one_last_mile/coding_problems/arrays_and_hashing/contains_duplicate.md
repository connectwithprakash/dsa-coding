# Contains Duplicate

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Examples
```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## My Approach
I need to detect if any number appears more than once. A HashSet is perfect for this - I can check if I've seen a number before in O(1) time:
1. Create an empty set to track seen numbers
2. For each number in the array:
   - If it's already in the set, I found a duplicate → return True
   - Otherwise, add it to the set
3. If I go through all numbers without finding duplicates → return False

## My Solution
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
```

## Complexity Analysis
- **Time Complexity**: O(n) - I iterate through the array once
- **Space Complexity**: O(n) - Worst case (no duplicates), my set stores all n elements

## What I Learned
- Set operations (lookup and insertion) are O(1) average case - perfect for this problem
- This is optimal because I must examine each element at least once
- The `else` clause in my solution is optional but makes the logic clearer

## Other Approaches I Considered
1. **Sorting**: O(n log n) time, O(1) space - Sort array then check if adjacent elements are equal
2. **Brute Force**: O(n²) time, O(1) space - Compare each element with every other (too slow!)