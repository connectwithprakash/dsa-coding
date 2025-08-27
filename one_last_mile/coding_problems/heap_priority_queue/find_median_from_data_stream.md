# Find Median from Data Stream

## Problem
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:
- `MedianFinder()` initializes the MedianFinder object
- `void addNum(int num)` adds the integer num from the data stream to the data structure
- `double findMedian()` returns the median of all elements so far

## My Approach

I divide the stream into two halves using two heaps:
- Max heap for the smaller half (left side)
- Min heap for the larger half (right side)

By maintaining these heaps with balanced sizes (differ by at most 1), I can find the median in O(1) time by looking at the roots of the heaps.

## Solution with Comments

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Stores smaller half (negated for max heap)
        self.min_heap = []  # Stores larger half

    def addNum(self, num: int) -> None:
        # Decide which heap to add to
        # If num is larger than the smallest in larger half, add to min_heap
        if self.max_heap and num > -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        # Balance the heaps to ensure size difference <= 1
        # Max heap can have at most 1 more element than min heap
        if len(self.max_heap) < len(self.min_heap):
            # Move smallest from larger half to smaller half
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - 1 > len(self.min_heap):
            # Move largest from smaller half to larger half
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # Even total elements: average of two middle values
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # Odd total elements: middle value is in max_heap
        else:
            return -self.max_heap[0]
```

## Improved Solution with Better Initial Placement

```python
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Smaller half
        self.min_heap = []  # Larger half

    def addNum(self, num: int) -> None:
        # Always add to max_heap first
        heapq.heappush(self.max_heap, -num)
        
        # Move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Balance if min_heap has more elements
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

## Visual Intuition

### Two-Heap Structure

```
Data stream: [5, 15, 1, 3, 8, 7, 9, 10, 20, 12]

After processing all numbers:
                    
Max Heap (smaller half)    |    Min Heap (larger half)
        8                   |         9
       / \                  |        / \
      7   5                 |      10   12
     / \                    |      / \
    1   3                   |    20   15
    
[-8, -7, -5, -1, -3]        |    [9, 10, 12, 20, 15]
(stored as negative)        |    (regular min heap)

Median = (8 + 9) / 2 = 8.5
```

### Step-by-Step Example

```
Stream: [5, 2, 8, 3, 9]

Add 5:
  max_heap: [-5]
  min_heap: []
  median: 5

Add 2:
  max_heap: [-2, -5] → balance → [-2]
  min_heap: [] → [5]
  median: (2 + 5) / 2 = 3.5

Add 8:
  max_heap: [-2]
  min_heap: [5, 8] → balance → [-5, -2]
  min_heap: [8]
  median: 5

Add 3:
  max_heap: [-5, -2, -3] → balance → [-3, -2]
  min_heap: [8] → [5, 8]
  median: (3 + 5) / 2 = 4

Add 9:
  max_heap: [-3, -2]
  min_heap: [5, 8, 9]
  balance → max_heap: [-5, -2, -3]
  min_heap: [8, 9]
  median: 5
```

## Why This Works

The algorithm maintains two invariants:
1. **Size invariant**: |max_heap| - |min_heap| ∈ {0, 1}
2. **Order invariant**: max(max_heap) ≤ min(min_heap)

These ensure:
- All elements in max_heap ≤ all elements in min_heap
- The median is always at the boundary between heaps
- Finding median is O(1) - just look at heap roots

## Complexity Analysis

### addNum
- **Time Complexity:** O(log n)
  - Heap insertions: O(log n)
  - At most 3 heap operations per add
  
### findMedian
- **Time Complexity:** O(1)
  - Just accessing heap roots
  
### Space Complexity
- **Space:** O(n)
  - Storing all n numbers across two heaps

## Edge Cases

```python
# Edge Case 1: Single element
finder = MedianFinder()
finder.addNum(1)
# median = 1

# Edge Case 2: Two elements
finder.addNum(2)
# median = (1 + 2) / 2 = 1.5

# Edge Case 3: All same values
[5, 5, 5, 5]
# median = 5

# Edge Case 4: Negative numbers
[-1, -2, -3]
# median = -2

# Edge Case 5: Large range
[1, 1000000]
# median = 500000.5
```

## Common Mistakes

1. **Wrong heap for initial insertion**:
   ```python
   # Wrong: Always adding to max_heap without checking
   heapq.heappush(self.max_heap, -num)
   
   # Better: Check where it belongs first
   if self.max_heap and num > -self.max_heap[0]:
       heapq.heappush(self.min_heap, num)
   ```

2. **Incorrect balancing condition**:
   ```python
   # Wrong: Allows size difference > 1
   if len(self.max_heap) > len(self.min_heap) + 1:
   
   # Correct: Maintain difference ≤ 1
   if len(self.max_heap) - 1 > len(self.min_heap):
   ```

3. **Forgetting negation for max heap**:
   ```python
   # Wrong: Treating as regular heap
   return self.max_heap[0]
   
   # Correct: Remember negation
   return -self.max_heap[0]
   ```

4. **Wrong median calculation for even count**:
   ```python
   # Wrong: Integer division
   return (-self.max_heap[0] + self.min_heap[0]) // 2
   
   # Correct: Float division
   return (-self.max_heap[0] + self.min_heap[0]) / 2
   ```

## Alternative Approaches

### 1. Sorted List (Less Efficient)
```python
class MedianFinder:
    def __init__(self):
        self.nums = []
    
    def addNum(self, num):
        bisect.insort(self.nums, num)  # O(n) insertion
    
    def findMedian(self):
        n = len(self.nums)
        if n % 2 == 0:
            return (self.nums[n//2-1] + self.nums[n//2]) / 2
        return self.nums[n//2]
```

### 2. Balanced BST
- Could use self-balancing BST with size tracking
- O(log n) insertion, O(log n) median finding
- More complex to implement

## Pattern Recognition

This problem demonstrates:
- **Two-heap pattern** - Dividing data for efficient access to middle
- **Online algorithm** - Processing streaming data
- **Invariant maintenance** - Keeping heaps balanced
- **Opposite heap types** - Max and min heaps working together

Similar problems:
- Sliding Window Median
- Find Median from Two Sorted Arrays
- Kth Largest Element in a Stream
- Design a Statistics Tracker

## Key Insights

1. **Two heaps maintain sorted halves** - No need to sort entire dataset

2. **Balance invariant is crucial** - Ensures median is always at heap boundaries

3. **Max heap for smaller half** - Counter-intuitive but necessary

4. **O(1) median access** - The main advantage over sorting

5. **Streaming capability** - Can process infinite streams

## What I Learned

The two-heap solution elegantly solves the streaming median problem by maintaining a invariant that the median is always at the boundary between two heaps. The key insight is that we don't need the entire dataset sorted - just maintaining two sorted halves with balanced sizes is sufficient. The pattern of using complementary data structures (max heap + min heap) to maintain a global property (median) is powerful and appears in many streaming algorithms. The balancing logic ensures we can always find the median in O(1) time while keeping insertions at O(log n).