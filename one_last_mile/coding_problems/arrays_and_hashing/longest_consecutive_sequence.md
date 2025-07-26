# Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

**Constraint**: You must write an algorithm that runs in O(n) time complexity.

## Examples
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0,1,2,3,4,5,6,7,8]. Therefore its length is 9.
```

## My Approach
I need to find the longest sequence of consecutive numbers. My strategy:

1. **Identify sequence starts**: A number is the start of a sequence if `num-1` doesn't exist in the array
2. **For each sequence start**: Count how long the consecutive sequence goes by checking `num+1`, `num+2`, etc.
3. **Track maximum**: Keep track of the longest sequence found

**Key insight**: Only start counting from actual sequence beginnings to avoid redundant work!

## My Solution
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Base case
        if len(nums) < 2:
            return len(nums)
        
        nums_set = set(nums)
        # Create array of start of the sequence numbers
        start_seq_nums = []
        for num in nums_set:
            if (num-1) in nums_set:
                continue
            else:
                start_seq_nums.append(num)
        
        # Go through each start seq num and find if the next item
        # is available progressively
        max_len = 1
        for start_seq_num in start_seq_nums:
            count = 1
            while (start_seq_num + count) in nums_set:
                count += 1
            max_len = max(max_len, count)
        
        return max_len
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Each number is visited at most twice (once to identify starts, once during sequence counting)
- **Space Complexity**: O(n) - Set storage and start sequence array

**Why it's O(n) time**: Even though there's a nested while loop, each number is only counted once across all sequences. The inner while loop runs at most n times total across all iterations.

### Example: Why Each Number is Visited At Most Twice

**Input**: `nums = [1, 2, 3, 100, 200]`

**Visit 1 - Finding sequence starts** (each number checked once):
- Check 1: `0` not in set → **sequence start** ✅
- Check 2: `1` in set → not start
- Check 3: `2` in set → not start  
- Check 100: `99` not in set → **sequence start** ✅
- Check 200: `199` not in set → **sequence start** ✅

**Visit 2 - Counting sequences** (each number visited at most once more):
- From start 1: Check 1→2→3→4(not found) 
  - Numbers 1,2,3 each visited once during counting
- From start 100: Check 100→101(not found)
  - Number 100 visited once during counting  
- From start 200: Check 200→201(not found)
  - Number 200 visited once during counting

**Total visits per number**:
- 1: visited twice (start check + counting)
- 2: visited twice (start check + counting) 
- 3: visited twice (start check + counting)
- 100: visited twice (start check + counting)
- 200: visited twice (start check + counting)

**Key insight**: Even though 2 and 3 aren't sequence starts, they're still only visited twice total. The nested while loop doesn't create O(n²) because each number is counted in exactly one sequence.

## Example Walkthrough
**Input**: `nums = [100, 4, 200, 1, 3, 2]`

**Step 1 - Create set**: `{100, 4, 200, 1, 3, 2}`

**Step 2 - Find sequence starts**:
- 100: `99` not in set → **start** ✅
- 4: `3` in set → not start ❌
- 200: `199` not in set → **start** ✅  
- 1: `0` not in set → **start** ✅
- 3: `2` in set → not start ❌
- 2: `1` in set → not start ❌

**Start sequence numbers**: `[100, 200, 1]`

**Step 3 - Count sequences**:
- From 100: 100 → 101 not found → length = 1
- From 200: 200 → 201 not found → length = 1
- From 1: 1 → 2 → 3 → 4 → 5 not found → length = 4

**Maximum length**: 4 ✅

## What I Learned
- **Sequence start detection**: Check if `num-1` exists to identify true sequence beginnings
- **Avoid redundant work**: Only count from sequence starts, not every number
- **Set for O(1) lookups**: Convert array to set for constant-time membership testing
- **Deduplication bonus**: Using set automatically handles duplicates

## Optimized Version (Without Extra Array)
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums_set = set(nums)
        max_len = 0
        
        for num in nums_set:
            # Only start counting if this is the beginning of a sequence
            if (num - 1) not in nums_set:
                current_num = num
                current_len = 1
                
                # Count consecutive numbers
                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_len += 1
                
                max_len = max(max_len, current_len)
        
        return max_len
```

**This version eliminates the extra `start_seq_nums` array**, but both approaches have the same time/space complexity.

## Why This Approach is Optimal
1. **Avoids sorting**: O(n log n) sorting would work but is slower
2. **Smart sequence detection**: Only processes each number once effectively
3. **Leverages hash set**: O(1) lookup time for consecutive number checking
4. **Handles duplicates**: Set automatically deduplicates input

## Key Insight
The brilliant part is recognizing that I should only start counting from sequence beginnings. This prevents counting the same sequence multiple times and ensures each number is processed at most twice, giving us true O(n) performance!

Your solution demonstrates excellent understanding of hash set optimization and sequence detection patterns! 🎯