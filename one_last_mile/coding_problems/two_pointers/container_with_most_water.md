# Container With Most Water

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that can hold the most water.

Return the maximum amount of water a container can store.

**Note**: You may not slant the container.

## Examples
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) that the container can contain is 49.

Input: height = [1,1]
Output: 1
```

## My Approach
I need to find two lines that form the largest container. A naive O(n²) approach would check every pair, but I can use **two pointers** for O(n):

1. **Start from both ends** - Widest possible container initially
2. **Calculate area** - `min(left_height, right_height) * width`
3. **Move the shorter pointer** - The shorter line limits the water, so move it inward to potentially find a taller line
4. **Track maximum** - Keep the largest area found

**Key insight**: Always move the pointer with the shorter height because moving the taller one can only decrease the area!

## My Solution
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx, jdx = 0, len(heights)-1
        most_water = 0
        while idx < jdx:
            most_water = max(most_water, min(heights[idx], heights[jdx])*(jdx-idx))
            if heights[idx] < heights[jdx]:
                idx += 1
            else:
                jdx -= 1
        return most_water
```

## Complexity Analysis ✅
- **Time Complexity**: O(n) - Single pass with two pointers
- **Space Complexity**: O(1) - Only using two pointer variables

## Example Walkthrough
**Input**: `height = [1,8,6,2,5,4,8,3,7]`

**Process**:
1. `idx=0(1), jdx=8(7)` → area = min(1,7) * 8 = 8 → move idx (shorter)
2. `idx=1(8), jdx=8(7)` → area = min(8,7) * 7 = 49 → move jdx (shorter)
3. `idx=1(8), jdx=7(3)` → area = min(8,3) * 6 = 18 → move jdx (shorter)
4. `idx=1(8), jdx=6(8)` → area = min(8,8) * 5 = 40 → move either
5. Continue until pointers meet...

**Maximum area**: 49 ✅

## Why This Greedy Strategy Works

### The Key Insight
**Why move the shorter pointer?**
- Area = `min(left, right) * width`
- The shorter line **limits** the water height
- Moving the taller pointer only decreases width without potential height increase
- Moving the shorter pointer gives us a chance to find a taller line

### Proof by Contradiction
If we move the taller pointer instead:
- Width decreases by 1
- Height is still limited by the shorter line (unchanged)
- Result: Area can only decrease or stay same
- We miss potential better solutions with the shorter pointer

## What I Learned
- **Greedy two-pointer strategy** - Not all two-pointer problems just compare values
- **Area optimization** - Always consider what limits the result (shorter height)
- **Proof thinking** - Understanding why the greedy choice works
- **Optimal substructure** - Each move eliminates suboptimal solutions

## Alternative Approaches I Considered

### Brute Force (Not Recommended)
```python
def maxArea(self, height: List[int]) -> int:
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area
```
**Complexity**: O(n²) time - Too slow for large inputs

## Key Insight
This problem demonstrates that **greedy algorithms can be optimal** when we can prove that each local choice leads to a global optimum. The insight that "the shorter line limits the area" makes the greedy choice obvious and correct.