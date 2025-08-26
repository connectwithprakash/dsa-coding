# Last Stone Weight

## Problem
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the two heaviest stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x

At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return 0.

## My Approach

I use a max heap to always access the two heaviest stones efficiently. Since Python only has min heap, I negate all values to simulate max heap behavior. I repeatedly extract the two largest stones, compute their difference, and reinsert if non-zero, until at most one stone remains.

## Solution with Comments

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # Convert to max heap using negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract two largest (most negative values)
            largest_stone = heapq.heappop(max_heap)
            second_largest_stone = heapq.heappop(max_heap)
            
            # Calculate difference (both are negative)
            weight_difference = abs(largest_stone - second_largest_stone)
            
            # Only push back if there's a remainder
            if weight_difference > 0:
                heapq.heappush(max_heap, -weight_difference)
        
        # Return remaining stone or 0 if empty
        return -max_heap[0] if max_heap else 0
```

## Corrected Solution

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap using negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop two largest stones (most negative values)
            first = heapq.heappop(max_heap)  # Negative of largest
            second = heapq.heappop(max_heap)  # Negative of second largest
            
            # If stones are different, push back the difference
            # first and second are negative, so second - first gives positive difference
            if first != second:
                heapq.heappush(max_heap, first - second)
        
        # Return last stone weight or 0
        return -max_heap[0] if max_heap else 0
```

## Visual Intuition

### Example: stones = [2,7,4,1,8,1]

```
Initial: [2, 7, 4, 1, 8, 1]
Max Heap (negated): [-8, -7, -4, -2, -1, -1]

Round 1: Pop -8 and -7
         8 vs 7 → difference = 1
         Push -1
         Heap: [-4, -2, -1, -1, -1]

Round 2: Pop -4 and -2
         4 vs 2 → difference = 2
         Push -2
         Heap: [-2, -1, -1, -1]

Round 3: Pop -2 and -2 (we have two -2s from merging)
         2 vs 2 → difference = 0
         Don't push anything
         Heap: [-1, -1, -1]

Round 4: Pop -1 and -1
         1 vs 1 → difference = 0
         Heap: [-1]

Result: 1 (single stone remaining)
```

### Max Heap Simulation with Negation

```
Original values: [8, 7, 4, 2, 1, 1]
                  ↓ (want max heap)
                  
Negated values: [-8, -7, -4, -2, -1, -1]
                  ↑ (use min heap)
                  
Most negative = Largest original
heappop() returns -8 (represents 8)
```

## Why This Works

The algorithm works because:
1. **Max heap property**: Always gives us the two largest stones
2. **Negation trick**: Python's min heap becomes max heap with negative values
3. **Difference handling**: Correctly simulates stone smashing rules
4. **Termination**: Guaranteed to reduce stones by at least 1 each round

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Initial heapify: O(n)
  - At most n-1 iterations (each reduces stones by at least 1)
  - Each iteration: 2 pops + 1 push = O(log n)
  - Total: O(n) + O(n log n) = O(n log n)
  
- **Space Complexity:** O(n)
  - Heap storage for n stones

## Edge Cases

```python
# Edge Case 1: Single stone
stones = [5]
# Result: 5 (return immediately)

# Edge Case 2: Two equal stones
stones = [3, 3]
# Result: 0 (both destroyed)

# Edge Case 3: All equal stones (even count)
stones = [2, 2, 2, 2]
# Result: 0 (all destroyed in pairs)

# Edge Case 4: All equal stones (odd count)
stones = [3, 3, 3]
# Result: 3 (one survives)

# Edge Case 5: Powers of 2
stones = [1, 2, 4, 8]
# 8 vs 4 = 4, 4 vs 2 = 2, 2 vs 1 = 1
# Result: 1
```

## Common Mistakes

1. **Forgetting to negate when pushing back**:
   ```python
   # Wrong: Pushes positive value
   heapq.heappush(max_heap, weight_difference)
   
   # Correct: Push negative value
   heapq.heappush(max_heap, -weight_difference)
   ```

2. **Not handling empty heap at end**:
   ```python
   # Wrong: Assumes heap has element
   return -max_heap[0]
   
   # Correct: Check if heap is empty
   return -max_heap[0] if max_heap else 0
   ```

3. **Pushing zero differences**:
   ```python
   # Inefficient: Pushes zeros
   heapq.heappush(max_heap, -weight_difference)
   
   # Better: Only push non-zero
   if weight_difference > 0:
       heapq.heappush(max_heap, -weight_difference)
   ```

4. **Wrong difference calculation**:
   ```python
   # Wrong: May give negative result
   difference = largest - second_largest
   
   # Correct: Ensure positive difference
   difference = abs(largest - second_largest)
   # Or: second - first (since first is more negative)
   ```

## Pattern Recognition

This problem demonstrates:
- **Heap simulation** - Simulating game/process with priority queue
- **Max heap via negation** - Working around Python's min-only heap
- **Greedy selection** - Always choosing extremes (largest stones)
- **Reduction problem** - Reducing collection to single element

Similar problems:
- Last Stone Weight II (minimize final weight - DP)
- Super Ugly Number (heap simulation)
- Merge K Sorted Lists (heap for selection)
- Find K Pairs with Smallest Sums

## Alternative Approach - Using Max Heap Module

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python 3.9+ has built-in max heap support
        # For older versions, use negation trick
        
        # Create max heap
        heap = stones[:]
        heapq._heapify_max(heap)  # Private method, not recommended
        
        while len(heap) > 1:
            x = heapq._heappop_max(heap)
            y = heapq._heappop_max(heap)
            if x != y:
                heapq._heappush_max(heap, x - y)
        
        return heap[0] if heap else 0
```

Note: It's better to use the negation approach as it's more portable.

## Key Insights

1. **Negation for max heap** - Standard Python pattern for max heap operations

2. **Heap maintains invariant** - After each operation, heap property preserved

3. **Guaranteed termination** - Each round reduces stone count by 1 or 2

4. **Order doesn't matter** - Only relative weights matter, not original positions

5. **Greedy is optimal** - Always smashing largest stones gives correct result

## What I Learned

The solution effectively simulates the stone smashing game using a max heap. The negation trick to convert Python's min heap to max heap behavior is a crucial pattern. The algorithm elegantly handles all cases including equal stones (resulting in 0 difference) and ensures we always work with the two largest available stones. This problem is a great example of heap-based simulation where we need repeated access to extremes.