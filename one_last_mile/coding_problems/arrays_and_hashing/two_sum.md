# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

## My Approach
I need to find two numbers that add up to the target. My strategy is to use a hashmap where:
- Key: `target - current_number` (what I need to find)  
- Value: current index

As I iterate through the array, I check if the current number exists as a key in my hashmap. If it does, that means I've found the complement I was looking for!

Base case: If array length is 2, the answer is always [0,1].

## My Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
            
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map:
                jdx = hash_map[num]        
                break 
            else:
                hash_map[(target-num)] = idx
                
        return [idx, jdx] if (idx < jdx) else [jdx, idx]
```

## Complexity Analysis
- **Time Complexity**: O(n) - I iterate through the array once
- **Space Complexity**: O(n) - I store complements in the hashmap

## What I Learned
- The key insight is storing `target - num` as the key, not the number itself
- When I find a match, `jdx` comes from the hashmap (earlier index) and `idx` is current (later index)
- I need to return indices in ascending order, so I check `idx < jdx`
- The base case handles the minimum input size efficiently

## Why This Works
When I encounter a number that's already a key in my hashmap, it means:
- I previously stored `target - some_previous_number` as a key
- Now I found `some_previous_number` 
- So: `target - some_previous_number + some_previous_number = target` ✓