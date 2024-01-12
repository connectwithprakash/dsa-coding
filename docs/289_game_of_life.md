# Game of Life

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The first thought is that if I have a copy of the `board` then I can just do a simple looping and do a look up of `neighbors` from `copy board` and make changes to the `original board`.

Now, to do inplace replacement we need some kind of mechanism to store information abot the change made to each cell based on the the cell's `current state` and `neighbors state`. This is to make sure than when we are updating any cell we have the information about its past state (if changed).

So, we use 2-bit grady code to map the `transition` of `state` from one to another. For eg. `(0,1)` means that the cell was previously dead and in the `next state` became alive and is represented by the value `2`. Now, whenever this cell comes as neighbor we know that we should not count it as `alive`.

| Current State | Next State | Representation |
| ------------- | ---------- | -------------- |
| 0             | 0          | 0              |
| 0             | 1          | 2              |
| 1             | 0          | 3              |
| 1             | 1          | 1              |

# Approach
<!-- Describe your approach to solving the problem. -->
The approach is divided in three steps.
1. Loop through each cell.
2. Count the number of `neighbors`. - `count_neighbors()`
2. Based `current_state`, number of alive neighbors compute the `next_state` and store the gray code mapping according to `transition_map`. - `decide_life()`
3. Now, we know the transition state (`curr_state` -> `next_state`). We can convert the matrix back to binary by running another loop.

# Complexity
- Time complexity: $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
![image.png](https://assets.leetcode.com/users/images/acc94df5-a8d6-4df2-9d5b-7b88f8a060e8_1705081231.3801515.png)

# Code
```
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
            ]
        transition_map = {
            (0, 0): 0, (0, 1): 2, (1, 0): 3, (1, 1): 1
        }
        
        def count_neighbors(idx, jdx):
            count = 0
            # Count living neighbors
            for neighbor in neighbors:
                kdx, ldx = idx+neighbor[0], jdx+neighbor[1]
                if 0<=kdx<m and 0<=ldx<n:
                    if board[kdx][ldx] == 1 or board[kdx][ldx] == 3:
                        count += 1
            # Decide life based on neighbors
            return count

        def decide_life(idx, jdx):
            curr_state = board[idx][jdx]
            alive_neighbors_count = count_neighbors(idx, jdx)
            
            if curr_state == 1:
                if alive_neighbors_count < 2:
                    next_state = 0
                if 1 < alive_neighbors_count < 4:
                    next_state = 1
                else:
                    next_state = 0
            else:
                if alive_neighbors_count == 3:
                    next_state = 1
                else:
                    next_state = 0

            key = (curr_state, next_state)
            board[idx][jdx] = transition_map[key]
            
        # Change board state to either of values 0, 1, 2, 3 based 
        # on the transition
        for idx in range(m):
            for jdx in range(n):
                decide_life(idx, jdx)

        # Change board state back to binary
        for idx in range(m):
            for jdx in range(n):
                if board[idx][jdx] == 1 or board[idx][jdx] == 2:
                    board[idx][jdx] = 1
                else:
                    board[idx][jdx] = 0

```
