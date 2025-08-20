# Time Based Key-Value Store

## Problem
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` Initializes the object
- `void set(String key, String value, int timestamp)` Stores the key with the value at the given time timestamp
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the one with the largest `timestamp_prev`. If there are no values, it returns `""`

Note: All timestamps of `set` are strictly increasing.

## My Approach

Since timestamps are strictly increasing, each key's values form a sorted list. This makes binary search perfect for finding the largest timestamp less than or equal to our target. The key insight is that after binary search, if we don't find an exact match, we need the element just before where our target would be inserted.

## Initial Solution (with Bug)

```python
class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.data[key])-1
        if right == -1:
            return ""
        
        while left <= right:
            mid = (left+right)//2
            mid_value, mid_timestamp = self.data[key][mid]
            if timestamp == mid_timestamp:
                return mid_value
            elif timestamp < mid_timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        # BUG: When left=0, self.data[key][left-1] accesses index -1
        # In Python, this wraps around to the last element!
        if self.data[key][left-1][1] < timestamp:
            return self.data[key][left-1][0]
        else:
            return ""
```

**The Bug:** When searching for a timestamp smaller than all stored timestamps, `left` ends at 0. Using `self.data[key][left-1]` then accesses index -1, which in Python returns the last element (wraparound), not what we intended!

## Corrected Solution

```python
from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Dictionary mapping key -> list of (value, timestamp) tuples
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps are strictly increasing, we can simply append
        # This maintains sorted order by timestamp
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Handle case where key doesn't exist
        if key not in self.data or len(self.data[key]) == 0:
            return ""
        
        values = self.data[key]
        left, right = 0, len(values) - 1
        
        # Binary search for the largest timestamp <= target timestamp
        while left <= right:
            mid = (left + right) // 2
            mid_value, mid_timestamp = values[mid]
            
            if timestamp == mid_timestamp:
                # Exact match found
                return mid_value
            elif timestamp < mid_timestamp:
                # Target timestamp is smaller, search left half
                right = mid - 1
            else:
                # Target timestamp is larger, search right half
                # This element could be our answer if nothing better exists
                left = mid + 1
        
        # After binary search:
        # - left points to where timestamp would be inserted
        # - right = left - 1 points to largest timestamp < target (if exists)
        # We want the element at position left-1 (same as right)
        
        if left > 0:
            # Found a valid timestamp <= target
            return values[left - 1][0]
        else:
            # No timestamp <= target exists (all timestamps are larger)
            return ""
```

## Visual Intuition

```
Example: key="foo" has timestamps [1, 4, 6, 10]

Get timestamp=5:
[1, 4, 6, 10]
 L     M   R    mid=6 > 5, right = mid-1

[1, 4]
 L  R           mid=1 < 5, left = mid+1
 M

[1, 4]
    LR          mid=4 < 5, left = mid+1
    M

[1, 4]
       L        left > right, exit
     R

left=2, values[left-1] = values[1] = (value_at_4, 4) ✓

Get timestamp=0:
[1, 4, 6, 10]
 LM    R        mid=1 > 0, right = mid-1

 R L            left > right, exit

left=0, left-1 invalid, return "" ✓

Get timestamp=10:
[1, 4, 6, 10]
 L     M   R    mid=6 < 10, left = mid+1

[1, 4, 6, 10]
          L R   mid=10 = 10, return value_at_10 ✓
          M
```

## Edge Cases

```python
# Edge Case 1: Empty key
timeMap.get("nonexistent", 5)  # Returns ""

# Edge Case 2: Timestamp before all values
timeMap.set("key", "value1", 10)
timeMap.get("key", 5)  # Returns ""

# Edge Case 3: Timestamp after all values
timeMap.set("key", "value1", 10)
timeMap.get("key", 20)  # Returns "value1"

# Edge Case 4: Exact timestamp match
timeMap.set("key", "value1", 10)
timeMap.get("key", 10)  # Returns "value1"

# Edge Case 5: Multiple values
timeMap.set("key", "value1", 10)
timeMap.set("key", "value2", 20)
timeMap.get("key", 15)  # Returns "value1"
timeMap.get("key", 25)  # Returns "value2"
```

## Complexity Analysis

### set() Operation
- **Time Complexity:** O(1)
  - Simple append to list (amortized O(1))
- **Space Complexity:** O(1)
  - Storing one new entry

### get() Operation  
- **Time Complexity:** O(log n) where n is number of timestamps for the key
  - Binary search through sorted timestamps
- **Space Complexity:** O(1)
  - Only using variables for binary search

### Overall Space
- **Space Complexity:** O(m × n)
  - m = number of unique keys
  - n = average number of timestamps per key

## Key Insights

1. **Strictly increasing timestamps** - This guarantee allows us to use simple append and maintain sorted order

2. **Binary search insertion point** - After binary search, `left` indicates where the element would be inserted, so `left-1` has our answer

3. **Index boundary checking** - Critical to check `left > 0` to avoid wraparound with negative indices

## Pattern Recognition

This problem combines:
- **Binary Search** - Finding position in sorted list
- **Design** - Creating efficient data structure
- **Boundary Handling** - Careful index management

## What I Learned

The bug in my initial solution taught me the importance of boundary checking after binary search. When `left` becomes 0, it means all elements are greater than our target, and we must handle this case explicitly. Python's negative indexing can mask bugs if we're not careful. The pattern of using `left-1` after binary search to find "largest element less than or equal to target" is common and worth remembering.