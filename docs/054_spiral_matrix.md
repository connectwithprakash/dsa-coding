# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The intution is really basic which is to understand that when we reach the boundary change the direction of the traversal according to the cyclic nature i.e. if right then down, if down then left, if left then up, and if up then again right.

# Approach
<!-- Describe your approach to solving the problem. -->
Two mechanism to change direction of traversal.

1. Outer boundry check using indices to change the direction of traversal.
2. Inner boundry check using the information about in which direction was the boundary cell traversed and use that as direction of traversal.

# Complexity
- Time complexity: $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
![performance](https://assets.leetcode.com/users/images/03c968c0-40cb-43b1-bb55-8f364f2704a7_1704836738.9944098.png)
# Code
```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_path = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }

        direction = "right"

        count = 0
        m, n = len(matrix), len(matrix[0])
        total_elems = m*n
        idx, jdx = 0, 0
        result = []
        while count < total_elems:
            if isinstance(matrix[idx][jdx], int):
                result.append(matrix[idx][jdx])
                matrix[idx][jdx] = direction
                count += 1
            else:
                direction = spiral_path[matrix[idx][jdx]]

            if direction == "right":
                jdx += 1
            elif direction == "down":
                idx += 1
            elif direction == "left":
                jdx -= 1
            elif direction == "up":
                idx -= 1
            
            if idx == -1 or idx == m or jdx == -1 or jdx == n:
                idx = max(0, min(idx, m-1))
                jdx = max(0, min(jdx, n-1))
                direction = spiral_path[direction]

        return result

```
