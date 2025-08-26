# K Closest Points to Origin

## Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## My Approach

I maintain a max heap of size k where the root is always the farthest point among the k closest points found so far. For each new point, if it's closer than the farthest point in the heap, I remove the farthest and add the new point. This ensures the heap always contains the k closest points.

## Solution with Comments

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  # Max heap to track k closest points
        
        for point_idx, point in enumerate(points):
            # Calculate squared distance (no need for sqrt since comparing)
            current_distance = point[0]**2 + point[1]**2
            
            if len(max_heap) == k:
                # Heap is full, check if current point is closer
                farthest_distance_in_heap = -max_heap[0][0]
                
                if current_distance >= farthest_distance_in_heap:
                    continue  # Current point is farther, skip it
                else:
                    heapq.heappop(max_heap)  # Remove farthest point
            
            # Add current point (negate distance for max heap behavior)
            heapq.heappush(max_heap, (-current_distance, point_idx))
        
        # Extract points using stored indices
        k_closest_points = [points[idx] for _, idx in max_heap]
        
        return k_closest_points
```

## Optimized Solution (Store Points Directly)

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            squared_distance = x*x + y*y
            
            if len(max_heap) < k:
                # Heap not full, add directly
                heapq.heappush(max_heap, (-squared_distance, x, y))
            elif squared_distance < -max_heap[0][0]:
                # Current point is closer than farthest in heap
                heapq.heapreplace(max_heap, (-squared_distance, x, y))
        
        # Extract points from tuples
        return [[x, y] for _, x, y in max_heap]
```

## Even Simpler Solution (Sort All)

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # For small inputs or when k is close to n, sorting might be simpler
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
```

## Visual Intuition

### Example: points = [[1,3], [-2,2], [5,-1]], k = 2

```
Step-by-step max heap operations:

Initial: Empty heap, k = 2

Point [1,3]: distance = 10
- Heap not full, add (-10, [1,3])
- Heap: [(-10, [1,3])]

Point [-2,2]: distance = 8
- Heap not full, add (-8, [-2,2])
- Heap: [(-10, [1,3]), (-8, [-2,2])]
- Root is -10 (farthest among k closest)

Point [5,-1]: distance = 26
- Heap full, 26 > 10 (farthest in heap)
- Don't add, skip
- Heap unchanged: [(-10, [1,3]), (-8, [-2,2])]

Result: [[1,3], [-2,2]]
```

### Max Heap Visualization

```
Why max heap for finding k smallest?

Points by distance: [8, 10, 26]
Want k=2 closest: [8, 10]

Max heap of size 2:
      -10        (farthest of the k closest)
       /
     -8          (closer point)

New point with distance 26:
- Compare with root (-10 → 10)
- 26 > 10, so skip

New point with distance 5:
- Compare with root (-10 → 10)
- 5 < 10, so replace root
```

## Complexity Analysis

### Max Heap Approach
- **Time Complexity:** O(n log k)
  - Process n points
  - Each heap operation is O(log k)
  - Best when k << n
  
- **Space Complexity:** O(k)
  - Heap stores at most k elements

### Sorting Approach
- **Time Complexity:** O(n log n)
  - Sort all n points
  - Better when k is close to n
  
- **Space Complexity:** O(1)
  - In-place sorting

## Edge Cases

```python
# Edge Case 1: k = 1 (single closest)
points = [[1,1], [2,2], [3,3]], k = 1
# Result: [[1,1]]

# Edge Case 2: k = n (all points)
points = [[1,1], [2,2]], k = 2
# Result: [[1,1], [2,2]]

# Edge Case 3: Points at same distance
points = [[1,0], [0,1], [-1,0], [0,-1]], k = 2
# All distance 1, any 2 are valid

# Edge Case 4: Origin point
points = [[0,0], [1,1]], k = 1
# Result: [[0,0]]

# Edge Case 5: Negative coordinates
points = [[-2,-2], [-1,-1], [1,1]], k = 1
# Result: [[-1,-1]]
```

## Common Mistakes

1. **Using min heap instead of max heap**:
   ```python
   # Wrong: Min heap keeps k farthest points
   heapq.heappush(heap, (distance, point))
   
   # Correct: Max heap keeps k closest points
   heapq.heappush(heap, (-distance, point))
   ```

2. **Confusing variable names**:
   ```python
   # Confusing: "min" for max heap root
   min_distance = -heap[0][0]
   
   # Clear: Descriptive name
   farthest_distance_in_heap = -heap[0][0]
   ```

3. **Recalculating heap root distance**:
   ```python
   # Inefficient: Recalculate from point
   idx = heap[0][1]
   distance = points[idx][0]**2 + points[idx][1]**2
   
   # Efficient: Use stored distance
   farthest_distance = -heap[0][0]
   ```

4. **Not using heapreplace**:
   ```python
   # Two operations:
   heapq.heappop(heap)
   heapq.heappush(heap, item)
   
   # One optimized operation:
   heapq.heapreplace(heap, item)
   ```

## Alternative Approach - Quickselect

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
        
        def quickselect(left, right, k):
            if left >= right:
                return
            
            # Partition around pivot
            pivot_idx = random.randint(left, right)
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            
            store_idx = left
            pivot_dist = distance(points[right])
            
            for i in range(left, right):
                if distance(points[i]) < pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            
            points[store_idx], points[right] = points[right], points[store_idx]
            
            # Recursively partition correct side
            if store_idx == k:
                return
            elif store_idx < k:
                quickselect(store_idx + 1, right, k)
            else:
                quickselect(left, store_idx - 1, k)
        
        quickselect(0, len(points) - 1, k)
        return points[:k]
```

Average O(n), worst case O(n²)

## Pattern Recognition

This problem demonstrates:
- **Fixed-size heap** - Maintaining exactly k elements
- **Max heap for minimum** - Counter-intuitive but efficient
- **Distance without sqrt** - Comparing squared distances is sufficient
- **Multiple valid approaches** - Heap vs sort vs quickselect tradeoffs

Similar problems:
- Top K Frequent Elements
- Find K Pairs with Smallest Sums
- Kth Largest Element in an Array
- K Closest Points to a Point

## Key Insights

1. **Squared distance suffices** - No need for sqrt when only comparing

2. **Max heap maintains k smallest** - Root is the threshold for inclusion

3. **heapreplace optimization** - Atomic pop+push when heap is full

4. **Meaningful names crucial** - `farthest_in_heap` vs `min` clarifies logic

5. **Algorithm choice depends on k** - Heap for small k, sort for large k

## What I Learned

The solution demonstrates how a max heap efficiently maintains the k smallest elements from a stream. The key insight is that the root of a max heap of size k represents the threshold - any new element must be smaller than the root to be included. Using meaningful variable names like `farthest_distance_in_heap` instead of `min_distance` makes the max heap logic much clearer. The pattern of using opposite heap type (max for finding minimums, min for finding maximums) is powerful for bounded selection problems.