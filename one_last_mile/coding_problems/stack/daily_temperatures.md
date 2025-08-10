# Daily Temperatures

## Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

## Examples
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation:
- Day 0 (73°): Next warmer day is day 1 (74°) → 1 day wait
- Day 1 (74°): Next warmer day is day 2 (75°) → 1 day wait  
- Day 2 (75°): Next warmer day is day 6 (76°) → 4 days wait
- Day 3 (71°): Next warmer day is day 5 (72°) → 2 days wait
- Day 4 (69°): Next warmer day is day 5 (72°) → 1 day wait
- Day 5 (72°): Next warmer day is day 6 (76°) → 1 day wait
- Day 6 (76°): No warmer day → 0
- Day 7 (73°): No warmer day → 0

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## My Thought Process

### Initial Observation
Looking at this problem, I need to find the **next warmer day** for each day. My first instinct was to use a brute force approach - for each day, scan forward until I find a warmer temperature. But that would be O(n²) in the worst case.

### Key Insight - "Next Greater Element" Pattern
After thinking more, I realized this is a classic **"next greater element"** problem. The question is: what data structure can efficiently help me find the next greater element?

### The Stack Revelation  
The breakthrough came when I thought about what information I need to track:
- **Waiting days**: Days that haven't found their warmer day yet
- **Order matters**: More recent days should be checked first when a warmer day arrives
- **Efficient removal**: When I find a warmer day, I need to quickly update multiple waiting days

This screamed **stack**! But what kind of stack?

### Monotonic Stack Strategy
The key insight: maintain a **monotonic decreasing stack** of temperatures that are still waiting for warmer days.

Here's why this works:
- When I encounter a **warmer temperature**, it resolves the wait for all recent cooler days
- When I encounter a **cooler temperature**, it just joins the waiting list
- The stack naturally maintains the order - most recent waiting days are on top

### The Algorithm Emerges
1. **Process each day**: Iterate through temperatures
2. **Handle warmer days**: While current temp > stack top, pop and calculate wait time  
3. **Add current day**: Push current day onto stack to wait for its warmer day
4. **Remaining elements**: Days left in stack never found a warmer day (result = 0)

## My Approach
I use a **monotonic decreasing stack** to efficiently track days waiting for warmer temperatures:

- Stack stores `(temperature, index)` tuples for days still waiting
- When current day is warmer than stack top, it resolves multiple waiting days
- Current day then joins the waiting list (pushed to stack)
- Stack maintains decreasing order of temperatures naturally

**Key insight**: This transforms an O(n²) "look ahead" problem into an O(n) "look back" problem using the stack's memory of previous days.

## My Solution with Detailed Comments
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with all zeros (no warmer day found)
        result = [0] * len(temperatures)
        # Stack to maintain days waiting for warmer temperatures
        # Each element is (temperature, index) tuple
        stack = []
        
        for idx, temp in enumerate(temperatures):
            # While current temperature is warmer than days waiting in stack
            # Pop those days and calculate their wait time
            while len(stack) and temp > stack[-1][0]:
                item = stack.pop()  # Get (temperature, day_index) of waiting day
                waiting_day_index = item[1]
                # Calculate days waited: current_day - waiting_day
                result[waiting_day_index] = (idx - waiting_day_index)
            
            # Add current day to stack - it's now waiting for its warmer day
            stack.append((temp, idx))

        # Days remaining in stack never found a warmer day (result stays 0)
        return result
```

## Complexity Analysis
- **Time Complexity**: O(n) - each element is pushed and popped from stack at most once
- **Space Complexity**: O(n) - stack can contain up to n elements in worst case (decreasing temperatures)

## Detailed Example Walkthrough
**Input**: `temperatures = [73,74,75,71,69,72,76,73]`

**Step-by-step execution**:

1. **Day 0 (73°)**: Stack empty → push `(73,0)` → Stack: `[(73,0)]`

2. **Day 1 (74°)**: 74 > 73 → pop `(73,0)`, set `result[0] = 1-0 = 1` → push `(74,1)` → Stack: `[(74,1)]`

3. **Day 2 (75°)**: 75 > 74 → pop `(74,1)`, set `result[1] = 2-1 = 1` → push `(75,2)` → Stack: `[(75,2)]`

4. **Day 3 (71°)**: 71 < 75 → no popping → push `(71,3)` → Stack: `[(75,2), (71,3)]`

5. **Day 4 (69°)**: 69 < 71 → no popping → push `(69,4)` → Stack: `[(75,2), (71,3), (69,4)]`

6. **Day 5 (72°)**: 
   - 72 > 69 → pop `(69,4)`, set `result[4] = 5-4 = 1`
   - 72 > 71 → pop `(71,3)`, set `result[3] = 5-3 = 2`  
   - 72 < 75 → stop popping → push `(72,5)` → Stack: `[(75,2), (72,5)]`

7. **Day 6 (76°)**:
   - 76 > 72 → pop `(72,5)`, set `result[5] = 6-5 = 1`
   - 76 > 75 → pop `(75,2)`, set `result[2] = 6-2 = 4`
   - Push `(76,6)` → Stack: `[(76,6)]`

8. **Day 7 (73°)**: 73 < 76 → no popping → push `(73,7)` → Stack: `[(76,6), (73,7)]`

**Final result**: `[1,1,4,2,1,1,0,0]` (remaining stack elements get 0)

## What I Learned
- **Monotonic stack pattern** - Powerful technique for "next greater/smaller element" problems
- **Transform problem perspective** - Convert "look ahead" to "look back" using stack memory
- **Tuple storage strategy** - Store both value and index when both are needed later
- **While loop for multiple pops** - One warmer day can resolve multiple waiting days
- **Natural edge case handling** - Remaining stack elements automatically get default value

## Key Problem-Solving Insights
1. **Pattern recognition** - Identifying this as "next greater element" was crucial
2. **Data structure choice** - Stack perfectly fits the "most recent first" requirement  
3. **Monotonic property** - Maintaining decreasing order enables efficient resolution
4. **Index tracking** - Storing both temperature and index enables wait time calculation
5. **Amortized analysis** - Each element pushed/popped once despite nested while loop

## Why This Solution is Elegant
- **Single pass**: O(n) time through one traversal
- **Space efficient**: O(n) space with practical optimization
- **Intuitive logic**: Stack represents "days still waiting"
- **Natural handling**: Edge cases handled automatically
- **Scalable pattern**: Works for any "next greater element" variant