# Intuition
The structure of Pascal's Triangle provides a clear recursive pattern: each row is built based on the sum of adjacent elements from the previous row. To generate a specific row, we can iteratively compute each value in place, reducing space usage compared to constructing the entire triangle.

# Approach
1. Initialize an array, `row_vals`, with a length of `rowIndex + 1` where all elements are set to 1.  
   Example: For `rowIndex = 4`, the initial array is `[1, 1, 1, 1, 1]`.  

2. For each row from 2 to `rowIndex`:
   - Use a variable `prev` to store the previous element while traversing the row.
   - Iterate through the indices of the row (from 1 to the current row index) and update each value in place:
     - Compute the new value as the sum of `prev` and the current value.
     - Update `prev` to the current value after the computation.

3. Return the updated array as the final row.

This approach avoids constructing all preceding rows, making it efficient in terms of space.

# Complexity
- **Time complexity:**  
  $$O(k^2)$$  
  - Here, \( k \) represents the `rowIndex`. The computation involves iterating over \( k \) rows, with each row requiring up to \( k \) updates. This results in a total of \( O(k^2) \) operations.

- **Space complexity:**  
  $$O(k)$$  
  - The space usage is limited to the `row_vals` array, which has a size of \( k + 1 \). No additional space is used for intermediate computations.

# Code
```python
"""
Generates the `rowIndex`-th row of Pascal's Triangle.

Args:
    rowIndex (int): The index of the row in Pascal's Triangle (0-indexed).

Returns:
    List[int]: The elements of the `rowIndex`-th row as a list.

Concept:
---------
Pascal's Triangle is a triangular array where:
1. The first and last elements of every row are 1.
2. Each inner element is the sum of the two elements directly above it in the previous row.

Steps:
------
1. Start with an array initialized to 1 with a length of `rowIndex + 1` (`[1] * (rowIndex + 1)`).
2. Use an iterative approach to calculate the row:
   - For each row (1 to `rowIndex`), iterate through the inner elements (indices 1 to `row - 1`).
   - Update each element in place by summing the current value with the previous value.
   - Use a `prev` variable to track the previous value while traversing the row.

Example:
---------
Input: rowIndex = 4
Output: [1, 4, 6, 4, 1]

Explanation:
Initial row: [1, 1, 1, 1, 1]  (rowIndex + 1 elements)
1st iteration: [1, 2, 1, 1, 1] (sum elements at indices 0 & 1, 1 & 2)
2nd iteration: [1, 3, 3, 1, 1] (sum elements at indices 0 & 1, 1 & 2, 2 & 3)
3rd iteration: [1, 4, 6, 4, 1] (sum elements at indices 0 & 1, 1 & 2, 2 & 3)
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with 1s
        row_vals = [1] * (rowIndex + 1)
        
        # Compute each row iteratively
        for idx in range(2, rowIndex + 1):
            # Track the previous value in the row
            prev = row_vals[0]
            for jdx in range(1, idx):
                curr = row_vals[jdx]
                # Update the current element
                row_vals[jdx] = prev + curr
                # Move to the next element
                prev = curr
        
        return row_vals

