# Koko Eating Bananas

## Problem
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## My Approach

The key insight I had was recognizing this as a binary search problem on the solution space rather than on an array. The eating rate forms a monotonic relationship with time needed:
- Lower eating rate → More hours needed (monotonically decreasing)
- Higher eating rate → Fewer hours needed

The possible eating rates range from 1 (slowest) to max(piles) (eating the largest pile in one hour). We binary search this range to find the minimum viable rate.

## Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search bounds: minimum 1 banana/hour, maximum is largest pile
        min_speed = 1
        max_speed = max(piles)
        optimal_speed = max_speed
        
        def calculate_hours_needed(eating_speed):
            """Calculate total hours needed at given eating speed"""
            total_hours = 0
            for pile_size in piles:
                # Ceiling division: rounds up to account for partial hours
                # If pile=7 and speed=3: needs 3 hours (3+3+1)
                hours_for_pile = (pile_size + eating_speed - 1) // eating_speed
                total_hours += hours_for_pile
            return total_hours
        
        # Binary search for minimum viable eating speed
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            hours_needed = calculate_hours_needed(mid_speed)
            
            if hours_needed > h:
                # Too slow - need to eat faster
                min_speed = mid_speed + 1
            else:
                # Fast enough - try to find slower speed
                optimal_speed = mid_speed
                max_speed = mid_speed - 1
        
        return optimal_speed
```

### Alternative: More Concise with Sum
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        
        while min_speed < max_speed:
            mid_speed = (min_speed + max_speed) // 2
            
            # Calculate total hours using sum with ceiling division
            hours_needed = sum((pile + mid_speed - 1) // mid_speed for pile in piles)
            
            if hours_needed > h:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed
        
        return min_speed
```

## Visual Intuition

```
Example: piles = [3, 6, 7, 11], h = 8

Possible eating speeds: 1 to 11 (max pile)

Speed vs Hours relationship:
Speed 1:  3 + 6 + 7 + 11 = 27 hours ❌ (> 8)
Speed 2:  2 + 3 + 4 + 6  = 15 hours ❌ (> 8)
Speed 3:  1 + 2 + 3 + 4  = 10 hours ❌ (> 8)
Speed 4:  1 + 2 + 2 + 3  = 8 hours  ✓ (= 8) <- Minimum!
Speed 5:  1 + 2 + 2 + 3  = 8 hours  ✓
Speed 6:  1 + 1 + 2 + 2  = 6 hours  ✓
...
Speed 11: 1 + 1 + 1 + 1  = 4 hours  ✓

Binary Search Process:
Step 1: left=1, right=11, mid=6
        hours=6 ≤ 8 ✓ Can go slower
        
Step 2: left=1, right=5, mid=3
        hours=10 > 8 ❌ Too slow
        
Step 3: left=4, right=5, mid=4
        hours=8 ≤ 8 ✓ Can go slower
        
Step 4: left=4, right=3
        left > right, return 4
```

## Ceiling Division Techniques

```python
# Three equivalent ways to compute ceiling division:

# Method 1: Manual check for remainder
hours = pile // speed
if pile % speed > 0:
    hours += 1

# Method 2: Integer-only formula (my preferred)
hours = (pile + speed - 1) // speed

# Method 3: Using math.ceil
hours = math.ceil(pile / speed)
```

Why `(pile + speed - 1) // speed` works:
- If pile is divisible by speed: adding (speed-1) doesn't affect the result
- If there's a remainder: adding (speed-1) pushes it to the next integer

Example: pile=7, speed=3
- Normal: 7 // 3 = 2 (but we need 3 hours)
- Formula: (7 + 3 - 1) // 3 = 9 // 3 = 3 ✓

## Complexity Analysis

- **Time Complexity:** O(n × log m) where n = number of piles, m = max pile value
  - Binary search iterations: O(log m)
  - Each iteration calculates hours: O(n)
  
- **Space Complexity:** O(1)
  - Only using variables for binary search bounds
  - No additional data structures

## Key Insights

1. **Binary search on answer space** - We're not searching in the input array but in the range of possible answers (1 to max_pile)

2. **Monotonic property** - The relationship between eating speed and time is monotonic, making binary search applicable

3. **Ceiling division importance** - Must round up because Koko can't eat partial hours (if 2.1 hours needed, it takes 3 hours)

4. **Optimal bounds** - Maximum speed needed is max(piles) because eating faster than the largest pile provides no benefit

## Common Pitfalls

1. **Integer division rounding** - Remember to use ceiling division, not floor
2. **Binary search bounds** - Start from 1, not 0 (can't eat 0 bananas/hour)
3. **Tracking the result** - Must track the minimum valid speed found

## Pattern Recognition

This problem demonstrates:
- **Binary Search on Solution Space** - Not searching an array but a range of valid answers
- **Monotonic Function** - Speed and time have inverse relationship
- **Optimization Problem** - Finding minimum/maximum that satisfies constraints

Similar problems:
- Capacity to Ship Packages
- Split Array Largest Sum
- Minimize Max Distance to Gas Station

## What I Learned

The elegance of this problem is recognizing that binary search isn't just for sorted arrays - it works on any monotonic function. Here, we're searching for the optimal value in a solution space where we can efficiently check if a value is valid. The ceiling division trick `(a + b - 1) // b` is also a useful pattern for integer-only arithmetic that I'll remember for future problems.