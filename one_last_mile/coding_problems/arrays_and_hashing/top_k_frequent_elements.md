# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Constraint**: `1 <= k <= number of distinct elements in nums`

## Examples
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Input: nums = [1,2,2,3,3,3], k = 2
Output: [3,2]
```

## My Approach
I need to find the k most frequent elements in O(n) time. My strategy uses a "bucket sort" approach:

1. **Count frequencies** - Use a hashmap to count each number's frequency
2. **Group by frequency** - Create buckets where frequency is the key, and numbers with that frequency are the values
3. **Collect top k** - Start from the highest frequency and collect numbers until I have k elements

The key insight: Since we have at most n distinct elements, frequencies range from 1 to n. I can use this bounded range to achieve O(n) time complexity.

## My Solution
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = defaultdict(int)
        # Count frequencies and track max frequency
        max_freq = 1
        for num in nums:
            num2freq[num] += 1
            max_freq = max(max_freq, num2freq[num])
        
        # Group numbers by their frequency (bucket sort)
        freq2nums = defaultdict(list)
        for num, freq in num2freq.items():
            freq2nums[freq].append(num)

        # Collect top k elements starting from highest frequency
        result = []
        for freq in range(max_freq, 0, -1):
            # Take only as many as needed to reach k elements
            result.extend(freq2nums[freq][:(k-len(result))])
            if len(result) == k:
                break
                
        return result
```

## Complexity Analysis
- **Time Complexity**: O(n) - Single pass to count + single pass to group + at most k elements collected
- **Space Complexity**: O(n) - Two hashmaps storing at most n elements total

## What I Learned
- **Bucket sort pattern**: When values have a bounded range (1 to n), I can use buckets for O(n) sorting
- **Frequency bucketing**: Group elements by frequency instead of sorting by frequency
- **Early termination**: Stop collecting once I have k elements
- **Slicing optimization**: Use `[:(k-len(result))]` to take exactly the number of elements needed

## Why This Works
- Frequencies are bounded: maximum frequency ≤ n (array length)
- By iterating from max_freq down to 1, I naturally get elements in descending frequency order
- The slice `[:(k-len(result))]` ensures I never exceed k elements

## Alternative Approaches I Considered

### Heap Approach (O(n log k))
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    # Use min-heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
```
**Complexity**: O(n log k) time - Slower than my bucket approach

### Sorting Approach (O(n log n))
```python
def topKFrequent(nums, k):
    count = Counter(nums)
    # Sort by frequency
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [num for num, freq in sorted_items[:k]]
```
**Complexity**: O(n log n) time - Much slower

## Key Insight
My bucket sort approach is optimal because:
- Frequencies have a natural bound (1 to n)
- No need to sort - just iterate from high to low frequency
- Achieves the required O(n) time complexity
- More efficient than heap or sorting approaches for this specific problem