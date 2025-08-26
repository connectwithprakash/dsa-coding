# Kth Largest Element in an Array

## Problem
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

## My Approach

I maintain a min heap of size k containing the k largest elements seen so far. The root of this min heap is always the kth largest element. For each new element, if it's larger than the root (smallest of the k largest), I replace the root with the new element.

## Solution with Comments

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []  # Min heap to track k largest elements
        
        for num in nums:
            if len(min_heap) == k:
                # Heap full: check if current number is larger than kth largest
                if num < min_heap[0]:
                    continue  # Smaller than kth largest, skip
                else:
                    heapq.heappop(min_heap)  # Remove current kth largest
            
            heapq.heappush(min_heap, num)
        
        return min_heap[0]  # Root is the kth largest
```

## Optimized Solution

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k) to build initial heap
        
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)  # Pop and push in one operation
        
        return min_heap[0]
```

## Alternative Solution - Using nlargest

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Built-in function that uses heap internally
        return heapq.nlargest(k, nums)[-1]
```

## Quickselect Solution (Average O(n))

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left, right, k_smallest):
            """Find kth smallest element"""
            if left == right:
                return nums[left]
            
            # Random pivot for better average case
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quickselect(left, pivot_index - 1, k_smallest)
            else:
                return quickselect(pivot_index + 1, right, k_smallest)
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # Move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            # Move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index
        
        # kth largest = (n-k)th smallest
        return quickselect(0, len(nums) - 1, len(nums) - k)
```

## Visual Intuition

### Example: nums = [3,2,1,5,6,4], k = 2

```
Step-by-step min heap operations:

Initial: Empty heap, k = 2

Process 3: heap = [3]
Process 2: heap = [2, 3]  (heap full now)

Process 1: 
- 1 < 2 (root), skip
- heap = [2, 3]

Process 5:
- 5 > 2 (root), pop 2, push 5
- heap = [3, 5]

Process 6:
- 6 > 3 (root), pop 3, push 6  
- heap = [5, 6]

Process 4:
- 4 < 5 (root), skip
- heap = [5, 6]

Result: heap[0] = 5 (2nd largest)
```

### Why Min Heap for Kth Largest?

```
Array: [3, 2, 5, 6, 4, 1]
Sorted: [1, 2, 3, 4, 5, 6]
                    ↑
                2nd largest

Min heap of k=2 largest:
      5    ← kth (2nd) largest
     /
    6      ← larger element

The root (minimum of the k largest) is the answer!
```

## Complexity Analysis

### Min Heap Approach
- **Time Complexity:** O(n log k)
  - Process n elements
  - Each heap operation is O(log k)
  - Optimal when k << n
  
- **Space Complexity:** O(k)
  - Heap stores exactly k elements

### Quickselect Approach
- **Time Complexity:** 
  - Average: O(n)
  - Worst: O(n²) if bad pivot choices
  
- **Space Complexity:** O(1)
  - In-place partitioning

### Sorting Approach
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) for in-place sort

## Edge Cases

```python
# Edge Case 1: k = 1 (find maximum)
nums = [3, 2, 1], k = 1
# Result: 3

# Edge Case 2: k = n (find minimum)
nums = [3, 2, 1], k = 3
# Result: 1

# Edge Case 3: All elements same
nums = [5, 5, 5, 5], k = 2
# Result: 5

# Edge Case 4: Negative numbers
nums = [-1, -5, -3, -2], k = 2
# Result: -2

# Edge Case 5: Single element
nums = [1], k = 1
# Result: 1

# Edge Case 6: Already sorted
nums = [1, 2, 3, 4, 5], k = 2
# Result: 4
```

## Common Mistakes

1. **Using max heap instead of min heap**:
   ```python
   # Wrong: Max heap would need size n-k+1
   heapq.heappush(heap, -num)  # Unnecessary negation
   
   # Correct: Min heap of size k
   heapq.heappush(heap, num)
   ```

2. **Wrong comparison logic**:
   ```python
   # Wrong: Comparing with wrong element
   if num > heap[0]:  # Should be <=
       continue
   
   # Correct: Skip if smaller than kth largest
   if num < heap[0]:
       continue
   ```

3. **Not maintaining exact size k**:
   ```python
   # Wrong: Heap grows unbounded
   heapq.heappush(heap, num)
   
   # Correct: Maintain size k
   if len(heap) == k:
       if num > heap[0]:
           heapq.heapreplace(heap, num)
   ```

4. **Returning wrong element**:
   ```python
   # Wrong: Thinking max is at end
   return heap[-1]
   
   # Correct: Min heap root is kth largest
   return heap[0]
   ```

## Pattern Recognition

This problem demonstrates:
- **Fixed-size heap** - Maintaining exactly k elements
- **Min heap for kth largest** - Counter-intuitive but efficient
- **Online algorithm** - Can process streaming data
- **Multiple algorithms** - Heap vs quickselect vs sort tradeoffs

Similar problems:
- Kth Smallest Element in Array (use max heap)
- Find K Closest Elements
- Top K Frequent Elements
- Kth Largest Element in a Stream

## Comparison of Approaches

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Min Heap | O(n log k) | O(k) | k << n, streaming data |
| Quickselect | O(n) avg | O(1) | One-time query, can modify array |
| Sorting | O(n log n) | O(1) | Small arrays, need multiple kth values |
| Max Heap | O(n log n) | O(n) | Not recommended |

## Key Insights

1. **Min heap for max problems** - Root of k-sized min heap is kth largest

2. **Heap size determines answer** - Maintaining exactly k elements is crucial

3. **heapreplace optimization** - Combines pop and push atomically

4. **Quickselect for one-time** - Better average case for single query

5. **Stream processing capability** - Heap approach works for continuous data

## What I Learned

The solution elegantly solves the kth largest problem using a min heap of size k. The key insight is that among the k largest elements, the minimum is the kth largest overall. This pattern of using the opposite heap type (min for largest, max for smallest) with bounded size is fundamental for selection problems. The approach is particularly powerful for streaming scenarios where we can't access all data at once, and when k is much smaller than n, making it more efficient than sorting.