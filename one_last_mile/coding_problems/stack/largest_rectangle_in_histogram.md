# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Examples
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area 10 and is formed by heights [5,6] with width 2.

Input: heights = [2,4]
Output: 4
Explanation: The largest rectangle is formed by height 2 with width 2, or height 4 with width 1.

Input: heights = [2,1,2]
Output: 3
Explanation: The largest rectangle is formed by height 1 with width 3.
```

## My Thought Process

### Initial Observation
For each bar, the largest rectangle including that bar is determined by:
- How far it can extend left (until hitting a shorter bar)
- How far it can extend right (until hitting a shorter bar)
- Its own height

### Key Realization
When processing bars from left to right:
- If current bar is **taller or equal** to previous: The previous bar can potentially extend through current position
- If current bar is **shorter**: The previous taller bars cannot extend past here - time to calculate their rectangles!

### The Stack Strategy
I need a stack to track bars that can still potentially extend rightward:
- **Push**: When bar is taller than stack top (increasing sequence)
- **Pop**: When bar is shorter (taller bars are blocked)
- **Track extension**: Store how far back each bar can extend

### Critical Insight
When popping bars due to a shorter bar, that shorter bar can extend **leftward** to wherever the popped bars started! This is because if the popped bar could extend there, so can the shorter current bar.

## My Approach
I use a **monotonic increasing stack** to track bars that can potentially form rectangles:

- Stack stores `(leftmost_extension_index, height)` for each bar
- When a shorter bar arrives, calculate rectangles for all taller bars (they can't extend further)
- The shorter bar inherits the leftmost position of the last popped bar
- Process remaining stack at the end (these bars extend to the array end)

**Key insight**: Each bar is pushed once and popped once, calculating its maximum rectangle when popped.

## My Solution with Detailed Comments
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack of (leftmost_extendable_index, height)
        max_area = 0
        
        for current_idx, current_height in enumerate(heights):
            # Track how far left the current bar can extend
            leftmost_idx = current_idx
            
            # Pop all bars taller than current (they can't extend past current)
            while len(stack) and (current_height < stack[-1][1]):
                # Calculate rectangle for the bar being popped
                bar_left_idx, bar_height = stack.pop()
                # Width: from bar's leftmost position to current (exclusive)
                width = current_idx - bar_left_idx
                area = width * bar_height
                max_area = max(max_area, area)
                # Current bar can extend at least as far left as popped bar
                leftmost_idx = bar_left_idx
            
            # Push current bar with its leftmost extendable position
            stack.append((leftmost_idx, current_height))
        
        # Process remaining bars (they all extend to the end)
        while len(stack):
            bar_left_idx, bar_height = stack.pop()
            # Width: from bar's leftmost position to array end
            width = len(heights) - bar_left_idx
            area = width * bar_height
            max_area = max(max_area, area)
        
        return max_area
```

## Complexity Analysis
- **Time Complexity**: O(n) - each bar is pushed and popped exactly once
- **Space Complexity**: O(n) - stack can contain at most n elements

## Detailed Example Walkthrough
**Input**: `heights = [2,1,5,6,2,3]`

**Step-by-step execution:**

1. **Index 0, height=2**: Stack empty → push `(0,2)` → Stack: `[(0,2)]`

2. **Index 1, height=1**: 
   - 1 < 2 → pop `(0,2)`, area = (1-0)×2 = 2
   - `leftmost_idx` becomes 0 (inherited from popped bar)
   - Push `(0,1)` → Stack: `[(0,1)]`

3. **Index 2, height=5**: 5 > 1 → push `(2,5)` → Stack: `[(0,1), (2,5)]`

4. **Index 3, height=6**: 6 > 5 → push `(3,6)` → Stack: `[(0,1), (2,5), (3,6)]`

5. **Index 4, height=2**:
   - 2 < 6 → pop `(3,6)`, area = (4-3)×6 = 6
   - 2 < 5 → pop `(2,5)`, area = (4-2)×5 = **10** ✓
   - `leftmost_idx` becomes 2 (inherited)
   - 2 > 1 → push `(2,2)` → Stack: `[(0,1), (2,2)]`

6. **Index 5, height=3**: 3 > 2 → push `(5,3)` → Stack: `[(0,1), (2,2), (5,3)]`

**Process remaining stack:**
- Pop `(5,3)`: area = (6-5)×3 = 3
- Pop `(2,2)`: area = (6-2)×2 = 8
- Pop `(0,1)`: area = (6-0)×1 = 6

**Maximum area**: 10

## Visual Intuition
```
Heights: [2,1,5,6,2,3]
         
     6
   5 █
   █ █   3
 2 █ █ 2 █
 █ █ █ █ █
 █ █ █ █ █
 
Largest rectangle: 5×2 = 10 (bars at indices 2,3)
```

## Complex Example Walkthrough
**Input**: `heights = [3,6,5,7,4,8,1,0]`

```
Visual representation:
           █         (height 8 at index 5)
       █   █         (height 7 at index 3)
   █   █   █         (height 6 at index 1)
   █ █ █   █         (height 5 at index 2)
   █ █ █ █ █         (height 4 at index 4)
 █ █ █ █ █ █         (height 3 at index 0)
 █ █ █ █ █ █         (height 2)
 █ █ █ █ █ █ █       (height 1 at index 6)
 0 1 2 3 4 5 6 7     (indices)
 3 6 5 7 4 8 1 0     (heights)
```

**Execution trace:**

1. **idx=0, h=3**: Push `(0,3)` → Stack: `[(0,3)]`

2. **idx=1, h=6**: 6>3 → Push `(1,6)` → Stack: `[(0,3), (1,6)]`

3. **idx=2, h=5**: 5<6 → Pop `(1,6)`, area=6×1=6, inherit idx=1 → Push `(1,5)` → Stack: `[(0,3), (1,5)]`

4. **idx=3, h=7**: 7>5 → Push `(3,7)` → Stack: `[(0,3), (1,5), (3,7)]`

5. **idx=4, h=4**:
   - 4<7 → Pop `(3,7)`, area=7×1=7
   - 4<5 → Pop `(1,5)`, area=5×3=**15** (from idx 1 to 4)
   - inherit idx=1, 4>3 → Push `(1,4)` → Stack: `[(0,3), (1,4)]`

6. **idx=5, h=8**: 8>4 → Push `(5,8)` → Stack: `[(0,3), (1,4), (5,8)]`

7. **idx=6, h=1**:
   - 1<8 → Pop `(5,8)`, area=8×1=8
   - 1<4 → Pop `(1,4)`, area=4×5=**20** ✓ (from idx 1 to 6)
   - 1<3 → Pop `(0,3)`, area=3×6=18
   - inherit idx=0 → Push `(0,1)` → Stack: `[(0,1)]`

8. **idx=7, h=0**:
   - 0<1 → Pop `(0,1)`, area=1×7=7
   - inherit idx=0 → Push `(0,0)` → Stack: `[(0,0)]`

**Final cleanup:**
- Pop `(0,0)`: area=0×8=0

**Maximum area**: 20 (height 4 spanning indices 1-5)

## What I Learned
- **Monotonic stack pattern** - Maintain increasing order to find boundaries
- **Leftward extension inheritance** - Shorter bars can extend where taller bars could
- **Two-phase processing** - Handle during iteration and cleanup at end
- **Rectangle width calculation** - Current position minus leftmost extension
- **Each bar processed once** - Push once, pop once, calculate area once

## Key Problem-Solving Insights
1. **Monotonic stack maintains potential** - Bars that might form larger rectangles later
2. **Popping means finalization** - Calculate area when bar can't extend further
3. **Index inheritance is crucial** - Enables leftward extension tracking
4. **End cleanup necessary** - Remaining bars extend to array boundary
5. **Single pass sufficiency** - No need for separate left/right scans