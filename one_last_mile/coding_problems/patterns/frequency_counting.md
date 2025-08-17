# Frequency Counting Pattern

## What is Frequency Counting?
A technique for solving problems by counting occurrences of elements, characters, or patterns. Often uses hash maps or arrays to track frequencies, enabling efficient lookups and comparisons.

## When to Use This Pattern

### Problem Characteristics
- Need to count occurrences
- Checking if two collections have same elements
- Finding most/least frequent elements
- Anagram or permutation problems
- Problems with "exactly k" or "at most k" distinct elements

### Keywords That Signal This Pattern
- "frequency"
- "count"
- "anagram"
- "permutation"
- "most/least common"
- "top k frequent"
- "occurrence"
- "duplicate"
- "unique"

## Core Data Structures

### 1. HashMap Counting
Most flexible, works with any hashable type.
```python
from collections import defaultdict, Counter

# Method 1: defaultdict
freq = defaultdict(int)
for item in array:
    freq[item] += 1

# Method 2: Counter (more Pythonic)
freq = Counter(array)
```

### 2. Array Counting (Bounded Input)
When input is bounded (e.g., lowercase letters, digits).
```python
# For lowercase letters
freq = [0] * 26
for char in string:
    freq[ord(char) - ord('a')] += 1
```

### 3. Bucket Sort Technique
For finding top k frequent elements.
```python
# Create buckets where index = frequency
buckets = [[] for _ in range(len(array) + 1)]
for value, freq in counter.items():
    buckets[freq].append(value)
```

## Problems I've Solved

### 1. Valid Anagram
**Pattern**: Compare frequency maps
**Key insight**: Anagrams have identical character frequencies
```python
# O(1) space for lowercase letters constraint
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
    for char in t:
        freq[ord(char) - ord('a')] -= 1
    
    return all(count == 0 for count in freq)
```

### 2. Group Anagrams
**Pattern**: Use frequency as key
**Key insight**: Create unique key from character frequencies
```python
def groupAnagrams(strs):
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Create frequency key
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Use tuple of frequencies as key
        key = tuple(freq)
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())
```

### 3. Top K Frequent Elements
**Pattern**: Bucket sort by frequency
**Key insight**: Use frequency as bucket index
```python
def topKFrequent(nums, k):
    freq = Counter(nums)
    
    # Buckets where index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Collect top k from highest frequency buckets
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[freq])
        if len(result) >= k:
            return result[:k]
```

### 4. Contains Duplicate
**Pattern**: Set for uniqueness checking
**Key insight**: Set size differs if duplicates exist
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

### 5. Permutation in String
**Pattern**: Sliding window with frequency matching
**Key insight**: Fixed window with frequency comparison
```python
def checkInclusion(s1, s2):
    s1_freq = Counter(s1)
    window_freq = Counter()
    
    for i in range(len(s2)):
        # Add to window
        window_freq[s2[i]] += 1
        
        # Remove from window if exceeds size
        if i >= len(s1):
            old_char = s2[i - len(s1)]
            window_freq[old_char] -= 1
            if window_freq[old_char] == 0:
                del window_freq[old_char]
        
        # Check if frequencies match
        if window_freq == s1_freq:
            return True
```

## Advanced Techniques

### Frequency Difference Tracking
Track differences instead of full frequencies:
```python
# For checking if window contains all characters of target
needed = len(target_freq)
formed = 0

for char in window:
    if char in target_freq:
        window_freq[char] += 1
        if window_freq[char] == target_freq[char]:
            formed += 1

# Window is valid when formed == needed
```

### Multiple Frequency Maps
Sometimes need to track multiple conditions:
```python
# Example: Find substrings with exactly k distinct characters
distinct_count = 0
freq = defaultdict(int)

for char in string:
    if freq[char] == 0:
        distinct_count += 1
    freq[char] += 1
    
    if distinct_count == k:
        # Valid window
```

### Frequency as Hash Key
Use frequency signature as dictionary key:
```python
# Group by frequency pattern
def frequency_key(s):
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
    return tuple(freq)  # Immutable for hashing
```

## Complexity Analysis
- **Time**: Usually O(n) for single pass
- **Space**: 
  - O(k) where k is distinct elements
  - O(1) for bounded input (e.g., 26 letters)

## Common Pitfalls

1. **Not handling zero frequencies** - Remove from dict when count reaches 0
2. **Using lists as dict keys** - Lists aren't hashable, use tuples
3. **Forgetting edge cases** - Empty input, single element
4. **Inefficient frequency comparison** - Direct dict comparison is O(k)

## Optimization Techniques

### 1. Early Termination
```python
# If finding anagram
if len(s) != len(t):
    return False  # Can't be anagrams
```

### 2. Bounded Input Optimization
```python
# Instead of HashMap for lowercase letters
freq = [0] * 26  # O(1) space and faster access
```

### 3. Counter Arithmetic
```python
from collections import Counter

# Counter supports arithmetic operations
counter1 = Counter(s1)
counter2 = Counter(s2)

# Subtract frequencies
diff = counter1 - counter2  # Positive differences only
```

## Visual Intuition

```
Finding anagrams of "abc" in "cbaebabacd":

String: c b a e b a b a c d
Window: [c b a] e b a b a c d
Freq:   {a:1, b:1, c:1} ✓ Match!

String: c [b a e] b a b a c d  
Freq:   {a:1, b:1, e:1} ✗ No match

String: c b a e b a [b a c] d
Freq:   {a:1, b:1, c:1} ✓ Match!
```

## Pattern Combinations

### Frequency + Sliding Window
Most common combination:
- Longest Substring with K Distinct Characters
- Permutation in String
- Find All Anagrams

### Frequency + Two Pointers
- Valid Anagram with sorted strings
- Comparing frequencies while traversing

## My Key Learnings

1. **Bounded input → Array, Unbounded → HashMap** - Choose the right structure
2. **Counter class is powerful** - Built-in arithmetic and most_common()
3. **Frequency signature as key** - Useful for grouping by pattern
4. **Zero frequency cleanup** - Important for accurate comparisons
5. **Bucket sort for top k** - O(n) alternative to O(n log k) heap

## Related Patterns
- **Sliding Window** - Often combined for substring problems
- **Bucket Sort** - For frequency-based sorting
- **Heap** - Alternative for top k problems