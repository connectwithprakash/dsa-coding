# Sliding Window Maximum

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

## Examples
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Input: nums = [1], k = 1
Output: [1]
```

## My Thought Process

### First Attempt: Standard Max Heap
My initial idea was to use a max heap to track the maximum in each window. At each step: remove the element leaving the window, add the new element, and get the max in O(log n).

**Problem**: Removing an arbitrary element from a heap is O(n), not O(log n). You can only efficiently remove the top element. This would make the overall complexity O(n²).

### Second Attempt: Two Pointers with Max Tracking  
I tried using two pointers where `jdx` tracks the window end and `idx` tracks the position of the current maximum element. When the max element leaves the window, find the new max by scanning.

**Problem**: In worst case (like descending array [5,4,3,2,1]), every time the max leaves, I'd scan the entire window to find the new max. This gives O(n) per window = O(n²) overall.

### Breakthrough: Heap with Lazy Cleanup
The key insight: instead of immediately removing elements when they leave the window, let them accumulate in the heap and clean up lazily when accessing the maximum.

Store `(value, index)` pairs and when getting the max, keep popping stale elements until finding one that's still in the current window.

## My Approach
I use a **max heap with lazy cleanup** to efficiently track the maximum in each sliding window:

- Store `(negative_value, index)` tuples in heap (negative for max heap behavior)
- When elements slide out of window, don't remove them immediately  
- Instead, lazily clean up stale elements when accessing the maximum
- Use index to determine if the current max is still in the window

**Key insight**: Lazy cleanup transforms impossible O(n) arbitrary deletions into efficient O(log n) deletions from the top, maintaining O(n log n) overall complexity.

## My Solution with Detailed Comments
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize max heap with first window using (negative_value, index) tuples
        # Negative values because Python has min heap, we want max heap behavior
        max_heap = [(-num, idx) for idx, num in enumerate(nums[:k])]
        heapq.heapify(max_heap)
        
        # First window's maximum is at heap top
        result = [-max_heap[0][0]]
        
        # Process remaining elements, sliding the window
        for idx in range(k, len(nums)):            
            # Add new element to heap with current index
            heapq.heappush(max_heap, (-nums[idx], idx))
            
            # Lazy cleanup: remove stale elements from heap top
            # Current window spans [idx-k+1, idx], so elements with index <= (idx-k) are stale
            while len(max_heap) and (max_heap[0][1] <= (idx-k)):
                heapq.heappop(max_heap)
            
            # After cleanup, heap top is guaranteed to be from current window
            max_item = max_heap[0]
            # Convert back from negative value and add to result
            result.append(-max_item[0])

        return result
```

## Complexity Analysis
- **Time Complexity**: O(n log n) - each element is added once and removed at most once from heap
- **Space Complexity**: O(k) average case, O(n) worst case due to potential accumulation of stale elements

## Example Walkthrough
**Input**: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`

1. **Initialize**: heap = [(-3,1), (-1,0), (1,2)], result = [3]
2. **idx=3 (-3)**: Add (-3,3), cleanup stale elements, max = 3, result = [3,3]
3. **idx=4 (5)**: Add (-5,4), max = 5, result = [3,3,5]
4. **idx=5 (3)**: Add (-3,5), max = 5, result = [3,3,5,5]
5. **idx=6 (6)**: Add (-6,6), max = 6, result = [3,3,5,5,6]
6. **idx=7 (7)**: Add (-7,7), max = 7, result = [3,3,5,5,6,7]

## What I Learned
- **Lazy cleanup strategy** - Don't remove stale elements immediately, clean up when needed
- **Index tracking in heap** - Store both value and position to determine element validity
- **Max heap simulation** - Use negative values in min heap to get max heap behavior
- **Amortized complexity** - Each element processed at most twice total
- **Problem-solving evolution** - Sometimes the obvious approach has subtle flaws that lead to better solutions

## Alternative Approaches
There's an optimal O(n) solution using a **deque (double-ended queue)** that maintains indices in decreasing order of their values. However, my heap approach is more intuitive, meets the problem's requirements, and demonstrates important problem-solving patterns.

## Key Implementation Details
- **Negative values** - Python's heapq is min heap, so negate values for max behavior  
- **Tuple ordering** - Heap orders by first element (value), second element (index) breaks ties
- **Boundary check** - Elements with `index <= (idx-k)` are outside current window [idx-k+1, idx]
- **Cleanup timing** - Clean up before accessing max to ensure validity