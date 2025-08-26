# Task Scheduler

## Problem
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of time that the CPU will need to finish all the given tasks.

## My Approach

I use a max heap to always process the most frequent task first (greedy approach) and a queue to manage tasks in cooldown. The key insight is that processing high-frequency tasks first minimizes idle time. When all tasks are in cooldown, I jump the clock to when the next task becomes available.

## Solution with Comments

```python
from collections import deque, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()  # Tasks in cooldown: (available_time, count)
        
        # Count frequency of each task
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        
        # Max heap of task counts (negative for max heap)
        max_heap = [-value for value in counter.values()]
        heapq.heapify(max_heap)
        
        clock = 0  # Current time
        
        while max_heap or queue:
            clock += 1
            
            if not max_heap:
                # All tasks in cooldown, jump to next available
                clock = queue[0][0]
            else:
                # Process most frequent task
                count = 1 + heapq.heappop(max_heap)  # Decrement count
                
                # If task has remaining executions, add to cooldown queue
                if count:
                    queue.append((clock + n, count))
            
            # Check if any task's cooldown has expired
            if queue and (clock == queue[0][0]):
                count = queue.popleft()[1]
                heapq.heappush(max_heap, count)
        
        return clock
```

## Alternative Solution - Mathematical Approach

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies
        frequencies = Counter(tasks)
        
        # Find maximum frequency
        max_freq = max(frequencies.values())
        
        # Count how many tasks have max frequency
        max_freq_count = sum(1 for freq in frequencies.values() if freq == max_freq)
        
        # Calculate minimum time needed
        # (max_freq - 1) * (n + 1) + max_freq_count
        # This represents the "frame" structure
        min_time = (max_freq - 1) * (n + 1) + max_freq_count
        
        # Can't be less than total number of tasks
        return max(min_time, len(tasks))
```

## Visual Intuition

### Example: tasks = ["A","A","A","B","B","B"], n = 2

```
Step-by-step simulation:

Initial: Counter = {A: 3, B: 3}
Max Heap: [-3, -3] (representing A and B)
Queue: []

Time 1: Process A (count=3)
- Heap: [-3] (B remaining)
- Queue: [(4, -2)] (A available at time 4)
- Output: A

Time 2: Process B (count=3)
- Heap: []
- Queue: [(4, -2), (5, -2)]
- Output: A B

Time 3: No tasks available (all in cooldown)
- Idle
- Output: A B idle

Time 4: A becomes available
- Heap: [-2] (A back)
- Process A
- Queue: [(5, -2), (7, -1)]
- Output: A B idle A

Continue...
Final: A B idle A B idle A B
Time: 8 units
```

### Cooldown Visualization

```
Task A appears 3 times, n=2 (must wait 2 units between A's)

Timeline:
A _ _ A _ _ A
↑     ↑     ↑
t=1   t=4   t=7

We can fill the gaps with other tasks:
A B C A B C A
```

### Why Max Heap?

```
High frequency first minimizes idle:

Good (max heap):     Bad (random):
A B A B A B          A A A B B B
No idle!             A idle A idle A B B B
                     More idle time!
```

## Complexity Analysis

- **Time Complexity:** O(m * log 26) where m is total tasks
  - At most m iterations (process each task once)
  - Heap operations on at most 26 unique tasks: O(log 26) = O(1)
  - Overall: O(m)
  
- **Space Complexity:** O(26) = O(1)
  - Counter for at most 26 tasks
  - Heap with at most 26 elements
  - Queue with at most 26 elements

## Edge Cases

```python
# Edge Case 1: No cooldown needed
tasks = ["A", "B", "C"], n = 0
# Result: 3 (execute all immediately)

# Edge Case 2: Single task type
tasks = ["A", "A", "A"], n = 2
# Result: 7 (A idle idle A idle idle A)

# Edge Case 3: Many unique tasks
tasks = ["A", "B", "C", "D", "E", "F"], n = 2
# Result: 6 (no idle needed, enough variety)

# Edge Case 4: n larger than unique tasks
tasks = ["A", "A", "B", "B"], n = 5
# Result: 11 (A B idle idle idle idle A B)

# Edge Case 5: Single task
tasks = ["A"], n = 10
# Result: 1
```

## Common Mistakes

1. **Forgetting to negate for max heap**:
   ```python
   # Wrong: Creates min heap
   max_heap = list(counter.values())
   
   # Correct: Negate for max heap
   max_heap = [-value for value in counter.values()]
   ```

2. **Not handling empty heap case**:
   ```python
   # Wrong: Crashes when heap empty
   count = heapq.heappop(max_heap)
   
   # Correct: Check if heap exists
   if not max_heap:
       clock = queue[0][0]
   ```

3. **Wrong cooldown calculation**:
   ```python
   # Wrong: Task available too soon
   queue.append((clock + n - 1, count))
   
   # Correct: Must wait n units
   queue.append((clock + n, count))
   ```

4. **Processing queue at wrong time**:
   ```python
   # Wrong: Check queue before incrementing clock
   if queue and clock == queue[0][0]:
   
   # Correct: Increment clock first, then check
   clock += 1
   if queue and clock == queue[0][0]:
   ```

## Pattern Recognition

This problem demonstrates:
- **Greedy scheduling** - Process most frequent tasks first
- **Cooldown management** - Track when tasks become available
- **Time simulation** - Model CPU cycles with clock variable
- **Heap + Queue combination** - Different data structures for different purposes

Similar problems:
- Reorganize String (similar greedy with cooldown)
- Rearrange String k Distance Apart
- CPU Task Scheduling variations
- Meeting Rooms III

## Key Insights

1. **Max frequency determines minimum time** - Most frequent task sets the lower bound

2. **Greedy is optimal** - Always processing highest count minimizes idle

3. **Clock jumping** - Skip idle periods by jumping to next available task

4. **Two-phase tracking** - Active tasks in heap, cooling tasks in queue

5. **Mathematical formula exists** - Can solve without simulation in some cases

## Alternative Approaches Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Heap + Queue | O(m) | O(1) | Handles all cases | More complex |
| Mathematical | O(n) | O(1) | Very fast | Harder to understand |
| Priority Queue only | O(m log m) | O(m) | Simpler | Less efficient |

## What I Learned

This problem combines multiple concepts: greedy algorithms, heap operations, and queue management for cooldown tracking. The key insight is that processing high-frequency tasks first minimizes idle time. The clock-jumping optimization when all tasks are in cooldown is particularly clever - it avoids simulating unnecessary idle cycles. Understanding that we need both a heap (for selecting tasks) and a queue (for managing cooldowns) shows how different data structures serve different purposes in complex scheduling problems. The mathematical solution reveals that there's often an elegant formula hiding behind simulation problems.