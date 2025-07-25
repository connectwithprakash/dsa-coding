# Valid Sudoku

## Problem Statement
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition  
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition

**Note**: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

## Examples
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

## My Approach
I need to validate three separate constraints: rows, columns, and 3x3 sub-boxes. My strategy:

1. **Check all rows** - Ensure no duplicates in each row
2. **Check all columns** - Ensure no duplicates in each column
3. **Check all 3x3 boxes** - Ensure no duplicates in each 3x3 sub-box

For each check, I use a hashmap to track seen numbers and return false immediately if I find a duplicate.

## My Solution
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(idx):
            counter = defaultdict(int)
            for jdx in range(9):
                char = board[idx][jdx]
                if char == '.':
                    continue
                elif counter[char]:
                    return False
                else:
                    counter[char] += 1
            return True
                
        def check_col(jdx):
            counter = defaultdict(int)
            for idx in range(9):
                char = board[idx][jdx]
                if char == '.':
                    continue
                elif counter[char]:
                    return False
                else:
                    counter[char] += 1
            return True
        
        def check_3x3_cube(idx, jdx):
            deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
            counter = defaultdict(int)
            for dx, dy in deltas:
                char = board[idx+dx][jdx+dy]
                if char == '.':
                    continue
                elif counter[char]:
                    return False
                else:
                    counter[char] += 1
            return True

        # Check rows
        for idx in range(9):
            if not check_row(idx):
                return False
                
        # Check columns
        for jdx in range(9):
            if not check_col(jdx):
                return False
                
        # Check 3x3 cube blocks
        for idx in range(1, 9, 3):
            for jdx in range(1, 9, 3):
                if not check_3x3_cube(idx, jdx):
                    return False
        
        return True
```

## Complexity Analysis
- **Time Complexity**: O(n²) where n = 9, so O(81) = O(1) - Actually constant time!
- **Space Complexity**: O(1) - Fixed size hashmaps (at most 9 elements each)

**Your solution meets the criteria!** ✅

## What I Learned
- **Constraint validation pattern**: Check each constraint separately for clarity
- **Delta coordinates**: Using relative offsets `(-1,-1), (-1,0), etc.` for 3x3 box traversal
- **Early termination**: Return false immediately when a violation is found
- **Sudoku indexing**: 3x3 boxes have centers at (1,1), (1,4), (1,7), (4,1), etc.

## Optimized Single-Pass Solution (Using DefaultDict)
```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)  
        boxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == '.':
                    continue
                
                # Calculate which 3x3 box this cell belongs to
                # Example: (4,5) -> (4//3)*3 + 5//3 = 1*3 + 1 = 4 (center box)
                # Example: (0,8) -> (0//3)*3 + 8//3 = 0*3 + 2 = 2 (top-right box)
                box_index = (i // 3) * 3 + j // 3
                
                # Check if number already exists in row, column, or box
                if char in rows[i] or char in cols[j] or char in boxes[box_index]:
                    return False
                
                # Add to respective sets
                rows[i].add(char)
                cols[j].add(char)
                boxes[box_index].add(char)
        
        return True
```

**This version is more efficient**: Single pass through the board instead of three separate passes.

## What I Learned From This Problem

### Box Indexing Formula Deep Dive
The formula `box_index = (i // 3) * 3 + j // 3` is brilliant! Let me break down how I understand it:

**Sudoku has 9 boxes arranged in a 3x3 grid of boxes:**
```
Box Layout:
[0] [1] [2]
[3] [4] [5] 
[6] [7] [8]
```

**How the formula works:**
- `i // 3` gives me which "row of boxes" I'm in (0, 1, or 2)
- `j // 3` gives me which "column of boxes" I'm in (0, 1, or 2)  
- `(i // 3) * 3` converts box row to starting index (0→0, 1→3, 2→6)
- Adding `j // 3` gives the exact box number

**Examples I worked through:**
- Cell (0,0): `(0//3)*3 + 0//3 = 0*3 + 0 = 0` → Box 0 ✅
- Cell (4,5): `(4//3)*3 + 5//3 = 1*3 + 1 = 4` → Box 4 (center) ✅
- Cell (8,8): `(8//3)*3 + 8//3 = 2*3 + 2 = 8` → Box 8 (bottom-right) ✅

### My Approach vs Optimized Approach
- **My approach**: Three separate validation passes (rows, columns, boxes)
- **Optimized approach**: Single pass checking all constraints simultaneously
- **Both work**, but single pass is more efficient in practice

### Problem-Solving Insights
- **Constraint validation pattern**: When multiple rules need to be checked, validate each one systematically
- **Early termination**: Return false as soon as any violation is found - no need to continue
- **Hash set vs defaultdict**: Both work for duplicate detection, defaultdict is cleaner for initialization
- **Delta coordinates for 3x3**: My delta approach with center coordinates works but is more complex than the box index formula

### Why My Solution Is Solid
1. **Meets complexity requirements**: O(n²) time, O(1) space ✅
2. **Handles all constraints**: Rows, columns, and 3x3 boxes
3. **Proper edge cases**: Correctly skips '.' empty cells
4. **Clean separation**: Each validation function has single responsibility
5. **Early exits**: Returns false immediately on finding duplicates

The box indexing formula is something I'll definitely remember for future grid-based problems!