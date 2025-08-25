# Kth Largest Element in a Stream

## Problem
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer k and the stream of integers nums.
- `int add(int val)` Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

## My Approach

I maintain a min heap of size k where the smallest element (root) is the kth largest. When adding a new element, if it's larger than the root, I replace the root. This ensures the heap always contains the k largest elements seen so far.

## Solution with Comments

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        # Add all numbers to heap
        for num in nums:
            if len(self.heap) >= k:
                # If heap full, only keep if larger than min
                min_val = heapq.heappop(self.heap)
                if num < min_val:
                    heapq.heappush(self.heap, min_val)
                else:
                    heapq.heappush(self.heap, num)
            else:
                # Heap not full, add directly
                heapq.heappush(self.heap, num)
    
    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            # Heap full: replace min if val is larger
            min_val = heapq.heappop(self.heap)
            if val < min_val:
                heapq.heappush(self.heap, min_val)
            else:
                heapq.heappush(self.heap, val)
        else:
            # Heap not full: add directly
            heapq.heappush(self.heap, val)
        
        # Peek at kth largest (min of heap)
        third_largest = heapq.heappop(self.heap)
        heapq.heappush(self.heap, third_largest)
        
        return third_largest
```

## Optimized Solution

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # Convert to heap in O(n)
        
        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # Maintain size k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Return kth largest (min of heap)
        return self.heap[0]
```

## Even More Optimized Solution

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Sort and take k largest
        self.heap = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Pop and push in one operation
        
        return self.heap[0]
```

## Visual Intuition

### Example: k=3, nums=[4,5,8,2]

```
Initial state after constructor:
nums = [4, 5, 8, 2], k = 3

Step 1: Heapify all elements
Heap: [2, 4, 5, 8]

Step 2: Keep only k=3 largest
Pop 2 → Heap: [4, 5, 8] (min heap structure)

Visual:     4      (4 is kth largest)
           / \
          5   8

add(3):
- 3 < 4, don't add
- Return 4

add(5):
- Push 5 → Heap: [4, 5, 8, 5]
- Pop 4 → Heap: [5, 5, 8]
- Return 5 (new kth largest)

add(10):
- Push 10 → Heap: [5, 5, 8, 10]  
- Pop 5 → Heap: [5, 8, 10]
- Return 5
```

### Why Min Heap Works

```
Stream: [9, 3, 5, 2, 8, 1, 7], k=3

Min heap of size k=3 maintains:
         [5]        ← kth (3rd) largest
        /   \
      [8]   [9]     ← larger elements

Elements < 5 are ignored
Elements ≥ 5 potentially replace the min
```

## Complexity Analysis

### Constructor
- **Time Complexity:** 
  - Heapify: O(n)
  - Remove n-k elements: O((n-k) log n)
  - Total: O(n log n)
  
### Add Method
- **Time Complexity:** O(log k)
  - Push and potentially pop from heap of size k
  
- **Space Complexity:** O(k)
  - Heap stores exactly k elements

## Edge Cases

```python
# Edge Case 1: k = 1 (find maximum)
k = 1, nums = [1, 2, 3]
# Heap always has [3], returns maximum

# Edge Case 2: Initial array smaller than k
k = 3, nums = [1, 2]
add(3) → returns 1 (only 3 elements total)

# Edge Case 3: Duplicate values
k = 2, nums = [5, 5, 5]
add(5) → returns 5

# Edge Case 4: Negative numbers
k = 2, nums = [-1, -2, -3]
add(0) → returns -1

# Edge Case 5: Empty initial array
k = 1, nums = []
add(1) → returns 1
```

## Common Mistakes

1. **Using max heap instead of min heap**:
   ```python
   # Wrong: Max heap makes finding kth largest O(k)
   # Correct: Min heap makes it O(1)
   ```

2. **Not maintaining exact size k**:
   ```python
   # Wrong: Heap grows unbounded
   heapq.heappush(self.heap, val)
   
   # Correct: Maintain size k
   if len(self.heap) > self.k:
       heapq.heappop(self.heap)
   ```

3. **Inefficient peek operation**:
   ```python
   # Inefficient: Pop and push
   result = heapq.heappop(self.heap)
   heapq.heappush(self.heap, result)
   
   # Efficient: Direct access
   return self.heap[0]
   ```

4. **Not handling heap smaller than k**:
   ```python
   # Wrong: Assumes heap has k elements
   return self.heap[0]
   
   # Correct: Check size first
   if len(self.heap) < self.k:
       heapq.heappush(self.heap, val)
   ```

## Pattern Recognition

This problem demonstrates:
- **Fixed-size heap** - Maintaining exactly k elements
- **Stream processing** - Handling continuous data
- **Min heap for kth largest** - Counterintuitive but efficient
- **Online algorithm** - Process elements as they arrive

Similar problems:
- Find Median from Data Stream (two heaps)
- Top K Frequent Elements
- K Closest Points to Origin
- Sliding Window Maximum

## Key Insights

1. **Min heap for max problems** - Finding kth largest uses min heap of size k

2. **Root is the answer** - The smallest of the k largest is the kth largest

3. **Fixed size efficiency** - Keeping exactly k elements makes operations O(log k)

4. **heapreplace optimization** - Combines pop and push in one operation

5. **Stream vs batch** - Different from finding kth largest in a static array

## What I Learned

The solution demonstrates how a min heap can efficiently track the kth largest element in a stream. The key insight is that we only need to maintain the k largest elements seen so far, and among these, the minimum is our answer. The heapreplace() function is particularly useful for maintaining a fixed-size heap. This pattern of using a heap with opposite ordering (min heap for largest, max heap for smallest) is common in streaming problems where we need to maintain a window of extreme values.