# Generate Parentheses

## Problem Statement
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Input: n = 2
Output: ["(())","()()"]
```

## My Approach
I visualize this problem as a **binary tree** where each node represents a choice: add '(' or add ')'. The key insight is that not all paths lead to valid parentheses - I need to **prune invalid branches** early.

My strategy uses **backtracking with DFS**:
- At each step, I have two choices: add opening bracket '(' or closing bracket ')'
- **Pruning condition 1**: Can't add ')' if it would exceed number of '(' (invalid)
- **Pruning condition 2**: Can't add '(' if I've already used n opening brackets
- **Base case**: When I've used exactly n closing brackets, I have a valid combination

**Key insight**: Every valid parentheses string must start with '(' and end with ')', so I can start the recursion with the first opening bracket already placed.

## My Tree Visualization
```
For n=3:
                    ""
                    |
                   "("                    (start here)
               /         \
           "(("           "()"
          /    \         /    \
       "((("   "(()"   "()("  "()|" (pruned: close > open)
        |      /  \    /   \
      "((()"  "(()()" "()(()" "()()"
        |       |       |       |
    "((()))"  "(()())"  "()(())"  "()()()"
                        ...more paths...
```

## My Solution with Detailed Comments
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def recursion(parantheses_str, char, open_count, closed_count):
            # Early pruning: if we have more closing than opening brackets, invalid path
            if closed_count > open_count:
                return
            
            # Build the current string by adding the character
            parantheses_str += char
            
            # Base case: we've used exactly n closing brackets (and n opening brackets)
            # This means we have a complete valid parentheses combination
            if closed_count == n:
                result.append(parantheses_str)
                return
            
            # Choice 1: Add opening bracket '(' if we haven't used all n yet
            if open_count < n:
                recursion(parantheses_str, '(', open_count + 1, closed_count)
            
            # Choice 2: Add closing bracket ')' if we haven't used all n yet
            # Note: the pruning condition at top ensures we don't exceed open_count
            if closed_count < n:
                recursion(parantheses_str, ')', open_count, closed_count + 1)
        
        # Start recursion with first opening bracket (every valid string starts with '(')
        # Initial state: empty string, about to add '(', counts: open=1, closed=0
        recursion("", '(', 1, 0)
        
        return result
```

## Complexity Analysis
- **Time Complexity**: O(4^n / √n) - This requires detailed explanation:
  - **Upper bound**: At each step, we have at most 2 choices (add '(' or add ')'), and we make 2n total choices → O(2^(2n)) = O(4^n)
  - **Actual complexity**: Not all paths are valid due to pruning. The number of valid parentheses combinations is the nth Catalan number: C_n = (1/(n+1)) * (2n choose n) ≈ 4^n / (√π * n^(3/2))
  - **Why Catalan numbers**: Each valid parentheses sequence corresponds to a way of parenthesizing expressions, which is counted by Catalan numbers
  - **Pruning effect**: Our early pruning (`closed_count > open_count`) eliminates many invalid branches, but we still visit all valid combinations plus some pruned invalid ones
  - **Final bound**: O(4^n / √n) accounts for generating all valid combinations plus the overhead of exploring some invalid paths

- **Space Complexity**: O(n) for recursion depth and string building (excluding output space)
  - **Recursion depth**: Maximum depth is 2n (when we build a complete string of length 2n)
  - **String building**: Each recursive call creates a new string, but this is O(n) per path
  - **Note**: Output space is O(4^n / √n) but is not counted in space complexity analysis

## Detailed Example Walkthrough
**Input**: `n = 2`

**Tree traversal**:
1. **Start**: `recursion("", '(', 1, 0)` → builds `"("`
   - `closed_count (0) ≠ n (2)`, continue recursion

2. **Level 1**: From `"("`
   - Branch A: `recursion("(", '(', 2, 0)` → builds `"(("`
   - Branch B: `recursion("(", ')', 1, 1)` → builds `"()"`

3. **Level 2A**: From `"(("`
   - Can't add more '(' (open_count = n = 2)
   - Only option: `recursion("((", ')', 2, 1)` → builds `"(()"`

4. **Level 2B**: From `"()"`
   - Branch A: `recursion("()", '(', 2, 1)` → builds `"()(`
   - Branch B: `recursion("()", ')', 1, 2)` → **PRUNED!** (closed_count > open_count)

5. **Level 3A**: From `"(()"`
   - Can't add more '(' (open_count = n = 2)  
   - Only option: `recursion("(()", ')', 2, 2)` → builds `"(())"`
   - **Base case reached**: closed_count = n = 2, add `"(())"` to result

6. **Level 3B**: From `"()(`
   - Can't add more '(' (open_count = n = 2)
   - Only option: `recursion("()(", ')', 2, 2)` → builds `"()()"`
   - **Base case reached**: closed_count = n = 2, add `"()()"` to result

**Final result**: `["(())", "()()"]`

## What I Learned
- **Backtracking pattern** - Explore all possibilities but prune invalid paths early
- **Tree visualization** - Helps understand the recursive structure and pruning points
- **Early pruning optimization** - `closed_count > open_count` eliminates entire subtrees
- **Base case design** - Use `closed_count == n` since every valid string ends with ')'
- **Initialization strategy** - Start with first '(' since all valid strings begin this way
- **Parameter passing** - Pass counts to track state without global variables

## Key Implementation Insights
- **Pruning condition placement** - Check `closed_count > open_count` at function start for early termination
- **String building approach** - Pass string by value and modify, allowing natural backtracking
- **Count management** - Track both opening and closing bracket counts separately
- **Recursive structure** - Two recursive calls represent the two choices at each decision point
- **Catalan number connection** - The number of valid parentheses combinations follows Catalan sequence

## Alternative Approaches
1. **Iterative with stack** - More complex state management
2. **Dynamic programming** - Overkill for generation problem  
3. **Generate all then filter** - Inefficient due to exponential invalid combinations

My backtracking approach is optimal for this generation problem, efficiently exploring only valid paths in the solution space.