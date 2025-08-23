# LRU Cache

## Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity
- `int get(int key)` Return the value of the key if it exists, otherwise return -1
- `void put(int key, int value)` Update the value of the key if it exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity, evict the least recently used key.

Both `get` and `put` must run in O(1) average time complexity.

## My Approach

I realized I need two things for O(1) operations:
1. A hash map for O(1) lookups by key
2. A doubly linked list to maintain LRU order

The key insight is using sentinel nodes (dummy head and tail) to eliminate edge cases when the list is empty or has one item. I maintain the invariant that the LRU item is always at head.next and the MRU item is at tail.prev.

## Solution with Meaningful Comments

```python
class Node:
    def __init__(self, key: int, value: int, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}  # O(1) node lookup by key
        
        # Sentinel nodes eliminate edge cases when list is empty or has one item
        # Maintains invariant: LRU at head.next, MRU at tail.prev
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
        self.capacity = capacity
    
    def _insert_node(self, key: int, value: int):
        # Always insert at tail.prev position - this is the MRU position
        # This maintains our LRU ordering automatically
        new_node = Node(key, value)
        previous_node = self.tail.prev
        
        # Four pointer updates to insert between previous_node and tail
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
        # Update hash map for O(1) future access
        self.cache[key] = new_node
    
    def _remove_node(self, key: int):
        node = self.cache[key]
        
        # Connect neighbors to bypass this node
        # Works even for single item due to sentinel nodes
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # Remove from hash map to maintain consistency
        del self.cache[key]
    
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].value
            
            # Access counts as use - move to MRU position
            # Remove from current position and reinsert at tail
            self._remove_node(key)
            self._insert_node(key, value)
            return value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key exists - update value and mark as recently used
            self._remove_node(key)
            self._insert_node(key, value)
        elif self.size < self.capacity:
            # Space available - just add the new item
            self._insert_node(key, value)
            self.size += 1
        else:
            # At capacity - sacrifice LRU item (always at head.next)
            # to make room for new item
            lru_key = self.head.next.key
            self._remove_node(lru_key)
            self._insert_node(key, value)
```

## Visual Intuition

### Data Structure Layout
```
Hash Map: {key: Node}
           ↓
Doubly Linked List with Sentinels:

head ←→ [LRU] ←→ ... ←→ [MRU] ←→ tail
 ↑                               ↑
dummy                          dummy
```

### Example Operations

#### Initial State (capacity = 3)
```
Operation: cache = LRUCache(3)

head ←→ tail
```

#### Put Operations
```
Operation: put(1, 10)
head ←→ [1:10] ←→ tail
cache: {1: Node(1,10)}

Operation: put(2, 20)
head ←→ [1:10] ←→ [2:20] ←→ tail
cache: {1: Node(1,10), 2: Node(2,20)}

Operation: put(3, 30)
head ←→ [1:10] ←→ [2:20] ←→ [3:30] ←→ tail
cache: {1: Node(1,10), 2: Node(2,20), 3: Node(3,30)}
         ↑ LRU              MRU ↑
```

#### Get Operation (Moves to MRU)
```
Operation: get(1) → returns 10

Before: head ←→ [1:10] ←→ [2:20] ←→ [3:30] ←→ tail
After:  head ←→ [2:20] ←→ [3:30] ←→ [1:10] ←→ tail
                 ↑ LRU              MRU ↑
```

#### Put with Eviction
```
Operation: put(4, 40)  // Cache is full, evict LRU

Before: head ←→ [2:20] ←→ [3:30] ←→ [1:10] ←→ tail
                 ↑ LRU
                 
Step 1: Remove LRU (key=2)
        head ←→ [3:30] ←→ [1:10] ←→ tail
        
Step 2: Insert new at MRU
        head ←→ [3:30] ←→ [1:10] ←→ [4:40] ←→ tail
                 ↑ LRU              MRU ↑
```

### Update Existing Key
```
Operation: put(3, 35)  // Update value and move to MRU

Before: head ←→ [3:30] ←→ [1:10] ←→ [4:40] ←→ tail
After:  head ←→ [1:10] ←→ [4:40] ←→ [3:35] ←→ tail
```

## Why Sentinel Nodes?

Without sentinels, we'd need special cases:
```python
# Without sentinels - complex edge cases:
if self.head is None:  # Empty list
    self.head = self.tail = new_node
elif self.head == self.tail:  # Single item
    # Special handling
else:  # Normal case
    # Regular insertion

# With sentinels - uniform handling:
# Always insert between tail.prev and tail
# No special cases needed!
```

## Complexity Analysis

### Time Complexity
- **get(key)**: O(1)
  - Hash map lookup: O(1)
  - Remove node: O(1)
  - Insert node: O(1)
  
- **put(key, value)**: O(1)
  - Hash map operations: O(1)
  - List operations: O(1)

### Space Complexity
- **Overall**: O(capacity)
  - Hash map: O(capacity) entries
  - Doubly linked list: O(capacity) nodes
  - Sentinel nodes: O(1)

## Edge Cases

```python
# Edge Case 1: Single capacity
cache = LRUCache(1)
cache.put(1, 1)
cache.put(2, 2)  # Evicts key 1
cache.get(1)     # Returns -1

# Edge Case 2: Update existing key
cache = LRUCache(2)
cache.put(1, 1)
cache.put(1, 10)  # Updates value, moves to MRU
cache.get(1)      # Returns 10

# Edge Case 3: Get non-existent key
cache = LRUCache(2)
cache.get(1)  # Returns -1

# Edge Case 4: Repeated access pattern
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # 1 becomes MRU
cache.put(3, 3)  # Evicts 2, not 1
```

## Key Insights

1. **Dual data structure design** - Hash map for speed, linked list for order
   
2. **Sentinel nodes pattern** - Eliminates all edge cases by ensuring there's always a prev/next

3. **Position invariant** - LRU always at head.next, MRU always at tail.prev

4. **Update strategy** - Remove and reinsert is simpler than moving nodes

5. **Key storage in nodes** - Storing keys in nodes enables eviction without reverse lookup

## Common Mistakes

1. **Forgetting to update size**:
   ```python
   # Wrong: Missing size increment
   elif self.size < self.capacity:
       self._insert_node(key, value)
       # Missing: self.size += 1
   ```

2. **Not handling update case**:
   ```python
   # Wrong: Treating update as new insertion
   def put(self, key, value):
       if self.size < self.capacity:
           self._insert_node(key, value)
       # Missing: Check if key exists first
   ```

3. **Incorrect eviction**:
   ```python
   # Wrong: Evicting from wrong end
   lru_key = self.tail.prev.key  # This is MRU!
   
   # Correct: Evict from head.next
   lru_key = self.head.next.key
   ```

4. **Not moving on get**:
   ```python
   # Wrong: Just returning value
   def get(self, key):
       return self.cache[key].value
   # Missing: Move to MRU position
   ```

## Pattern Recognition

This problem demonstrates:
- **Cache design** - Balancing fast access with capacity constraints
- **LRU eviction policy** - Common in OS page replacement, database buffers
- **Composite data structures** - Combining structures for optimal performance

Similar problems:
- LFU Cache (Least Frequently Used)
- Design HashMap
- Design LinkedList
- All O(1) Data Structure

## Alternative Approach - OrderedDict

Python's `OrderedDict` maintains insertion order and can be used for a simpler implementation:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end (MRU position)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # Remove first item (LRU)
                self.cache.popitem(last=False)
```

While simpler, understanding the manual implementation teaches valuable lessons about data structure design.

## What I Learned

The LRU Cache beautifully combines two data structures to achieve O(1) operations. The hash map provides instant access while the doubly linked list maintains temporal order. The sentinel nodes pattern was crucial - they eliminate all edge cases by ensuring every real node always has both prev and next neighbors. This problem taught me that complex requirements often need composite data structures, and that careful invariant maintenance (LRU at head.next, MRU at tail.prev) simplifies implementation logic.