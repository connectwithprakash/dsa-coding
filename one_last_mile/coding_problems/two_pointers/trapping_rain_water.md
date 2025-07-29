# Trapping Rain Water

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
```

## My Approach
Water trapped at any index depends on the **boundaries** (tallest bars) to its left and right. The water level at index `i` is `min(max_left[i], max_right[i]) - height[i]`.

I can solve this in three ways:
1. **Precompute boundaries** - Use two arrays to store left/right max heights
2. **Two pointers dual-pass** - Process boundaries with two separate passes
3. **Two pointers single-pass** - Optimal approach with single pass

## My Solution 1: Precompute Boundaries
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n  # Store max height to the left of each index
        max_right = [0]*n  # Store max height to the right of each index
        
        # Build both arrays simultaneously in one loop
        for l2r_idx in range(n):
            r2l_idx = (n-1-l2r_idx)  # Mirror index for right-to-left processing
            
            if l2r_idx == 0:
                # Base case: first element has no left neighbor, last element has no right neighbor
                max_left[l2r_idx] = height[l2r_idx]
                max_right[r2l_idx] = height[r2l_idx]
            else:
                # For each position, max is either current height or previous max
                max_left[l2r_idx] = max(height[l2r_idx], max_left[l2r_idx-1])
                max_right[r2l_idx] = max(height[r2l_idx], max_right[r2l_idx+1])
                
        # Calculate water trapped at each position
        total_water = 0
        for idx in range(n):
            # Water level is limited by the shorter of the two boundaries
            water_level = min(max_left[idx], max_right[idx])
            water_at_idx = water_level - height[idx]
            total_water += max(0, water_at_idx)  # Only add positive water (can't have negative)
        
        return total_water
```
**Complexity**: O(n) time, O(n) space

## My Solution 2: Two Pointers Dual-Pass
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        n = len(height)
        
        # First pass: Process areas where left boundary <= right boundary
        head, tail = 1, 0  # head searches for right boundary, tail is left boundary
        while head < n:
            if height[tail] <= height[head]:
                # Found a valid container: left boundary <= right boundary
                max_possible_water = min(height[head], height[tail])  # Water level is limited by shorter boundary
                
                # Fill all positions between the boundaries
                while tail < head:
                    water_at_idx = max_possible_water - height[tail]
                    total_water += max(0, water_at_idx)  # Only add positive water
                    tail += 1
                head += 1  # Move to next potential container
            else:
                # Right boundary is too short, keep searching
                head += 1
                
        # Second pass: Process areas where left boundary > right boundary  
        head, tail = n-2, n-1  # head searches for left boundary, tail is right boundary
        while head > -1:
            if height[tail] < height[head]:
                # Found a valid container: right boundary < left boundary (covers remaining cases)
                max_possible_water = min(height[head], height[tail])  # Water level is limited by shorter boundary
                
                # Fill all positions between the boundaries
                while tail > head:
                    water_at_idx = max_possible_water - height[tail]
                    total_water += max(0, water_at_idx)  # Only add positive water
                    tail -= 1
                head -= 1  # Move to next potential container
            else:
                # Left boundary is too short, keep searching
                head -= 1
        
        return total_water
```
**Complexity**: O(n) time, O(1) space
**Note**: Complex dual-pass approach with mutually exclusive conditions - no double counting

## My Solution 3: Optimal Two Pointers Single-Pass
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = height[0]  # Track maximum height seen from left
        max_r = height[n-1]  # Track maximum height seen from right

        total_water = 0

        idx = 0  # Left pointer
        jdx = n-1  # Right pointer
        while idx < jdx:
            # Update max heights as we encounter them
            max_l = max(max_l, height[idx])
            max_r = max(max_r, height[jdx])
            
            # Process the side with smaller max height (limiting factor)
            if max_l <= max_r:
                # Left side is limiting, safe to calculate water at left position
                total_water += max(0, min(max_l, max_r) - height[idx])
                idx += 1
            else:
                # Right side is limiting, safe to calculate water at right position
                total_water += max(0, min(max_l, max_r) - height[jdx])
                jdx -= 1

        return total_water
```
**Complexity**: O(n) time, O(1) space
**This is the optimal solution!** ✅

## What I Learned From My Solutions

### Solution Comparison
| Approach | Time | Space | Complexity | Notes |
|----------|------|-------|------------|-------|
| **Solution 1** | O(n) | O(n) | Medium | Good for understanding concept |
| **Solution 2** | O(n) | O(1) | High | Dual-pass, complex but correct |
| **Solution 3** | O(n) | O(1) | Low | Single-pass, optimal and elegant |

### Key Insights About Water Trapping
- **Water level = min(left_max, right_max)** - Limited by shorter boundary
- **Water trapped = max(0, water_level - height[i])** - Can't be negative
- **Need boundaries on both sides** - Water flows out without proper containment

### Why Solution 3 is Optimal
- **Process the side with smaller max height** - We know it's the limiting factor
- **Update max heights as we go** - No need to precompute
- **Single pass through array** - More efficient than dual-pass
- **Clean and intuitive logic** - Easy to understand and implement

When `max_l <= max_r`, we know the left side is the limiting factor, so it's safe to calculate water at the left position. The greedy approach ensures we never miss any trapped water while using constant space.