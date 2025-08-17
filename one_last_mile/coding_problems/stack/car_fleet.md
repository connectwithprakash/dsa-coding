# Car Fleet

## Problem Statement
There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`. 

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car. A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

## Examples
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: 
- Cars at 10 (speed 2) and 8 (speed 4) become a fleet, meeting at 12
- Car at 0 (speed 1) is a fleet by itself
- Cars at 5 (speed 1) and 3 (speed 3) become a fleet, meeting at 6
Total: 3 fleets

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: Single car forms one fleet

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation: All cars eventually merge into one fleet before reaching target
```

## My Thought Process

### Initial Understanding
I need to figure out how many distinct groups of cars will arrive at the destination. The key constraint is that cars cannot pass each other - when a faster car catches a slower one, they merge into a fleet moving at the slower speed.

### Key Realization
Initially, I thought cars would form a chain (one behind another), but that's wrong! When cars catch up, they **merge side-by-side** and travel together as a single unit at the same position. This changes everything about fleet formation.

### The Insight
To determine fleets, I need to know:
1. Which car will reach the target first (closest to target)
2. Whether cars behind can catch up before that car reaches the target
3. If they can't catch up in time, they form a separate fleet

### Algorithm Strategy
1. **Sort by position**: Process cars from closest to target to furthest
2. **Track fleet leader**: The car that determines arrival time for the fleet
3. **Check catch-up**: Can the next car reach the target in the fleet leader's time?
4. **Fleet formation**: If yes, join fleet; if no, become new fleet leader

## My Approach
I process cars from closest to target to furthest, checking if each car can catch up to the current fleet before it reaches the destination.

My strategy:
- Sort cars by position to process in order
- Track the current fleet leader (determines arrival time)
- For each car, calculate where it would be when the fleet leader reaches target
- If it reaches or passes target, it joins the fleet
- Otherwise, it becomes a new fleet leader

**Key insight**: A car joins a fleet only if it can reach the target within the fleet leader's arrival time.

## My Solution with Detailed Comments
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort car indices by position (ascending order)
        # We'll process from closest to target (via pop from end)
        cars_by_position = sorted(range(len(position)), key=position.__getitem__)
        
        current_fleet_leader_idx = None
        total_fleets = 0
        
        while len(cars_by_position):
            if current_fleet_leader_idx is None:
                # Start a new fleet with the car closest to target
                current_fleet_leader_idx = cars_by_position.pop()
                total_fleets += 1
                continue
            else:
                # Check if next car can join current fleet
                next_car_idx = cars_by_position.pop()
            
            # Calculate time for fleet leader to reach target
            fleet_time_to_target = (target - position[current_fleet_leader_idx]) / speed[current_fleet_leader_idx]
            
            # Calculate where this car would be when fleet leader reaches target
            next_car_position_at_fleet_arrival = position[next_car_idx] + (speed[next_car_idx] * fleet_time_to_target)
            
            if next_car_position_at_fleet_arrival < target:
                # Car doesn't reach target in time - becomes new fleet leader
                current_fleet_leader_idx = None
                # Push back to process as new fleet in next iteration
                cars_by_position.append(next_car_idx)

        return total_fleets
```

## Complexity Analysis
- **Time Complexity**: O(n log n) - dominated by sorting the positions
- **Space Complexity**: O(n) - for storing the sorted indices

## Detailed Example Walkthrough
**Input**: `target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`

**After sorting by position**: indices = [2,4,3,1,0] (positions: 0,3,5,8,10)

**Processing (from closest to target):**

1. **Car at position 10** (idx=0, speed=2):
   - Becomes fleet leader #1
   - Time to target: (12-10)/2 = 1 hour

2. **Car at position 8** (idx=1, speed=4):
   - Fleet leader reaches target in 1 hour
   - This car's position after 1 hour: 8 + 4×1 = 12 ✓
   - **Joins fleet #1**

3. **Car at position 5** (idx=3, speed=1):
   - Fleet leader reaches target in 1 hour
   - This car's position after 1 hour: 5 + 1×1 = 6 < 12 ✗
   - **Becomes fleet leader #2**
   - Time to target: (12-5)/1 = 7 hours

4. **Car at position 3** (idx=4, speed=3):
   - Fleet leader #2 reaches target in 7 hours
   - This car's position after 7 hours: 3 + 3×7 = 24 > 12 ✓
   - **Joins fleet #2**

5. **Car at position 0** (idx=2, speed=1):
   - Fleet leader #2 reaches target in 7 hours
   - This car's position after 7 hours: 0 + 1×7 = 7 < 12 ✗
   - **Becomes fleet leader #3**

**Result**: 3 fleets

## What I Learned
- **Fleet formation is side-by-side**, not sequential chains
- **Sort by position** to process cars in spatial order
- **Stack-like processing** with pop/append elegantly handles fleet transitions
- **Time-based checking** via position calculation determines fleet membership
- **Cars cannot pass** is the crucial constraint that creates distinct fleets

## Alternative Approach
The standard solution compares **time to reach target** directly:
```python
def carFleet(self, target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)  # Sort by position descending
    fleets = 0
    prev_time = 0
    
    for pos, spd in cars:
        time_to_target = (target - pos) / spd
        if time_to_target > prev_time:  # Can't catch up
            fleets += 1
            prev_time = time_to_target
    
    return fleets
```

Both approaches are mathematically equivalent - mine checks position at arrival time, the standard checks arrival time directly.

## Key Problem-Solving Insights
1. **Understanding "cannot pass"** - This creates the fleet formation behavior
2. **Side-by-side merging** - Not sequential following
3. **Processing order matters** - Start from closest to target
4. **Time vs Position** - Can check either arrival time or position at fleet arrival
5. **Stack pattern** - Using append/pop for fleet leader transitions