# [Python | Beats 100%] Simple and efficient solution to "Maximum Width of Binary Tree"

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My idea was to capture the start and end index in an array of the nodes at each level and subtract the index of left most node from the right most node and add 1 to get the level width.

# Approach
**BFS**
<!-- Describe your approach to solving the problem. -->
We create a queue that stores a tuple of `node` and its `index`. Here, we calculate the index using its parent index(i) as following:
* left child: `2*i+1`
* right child: `2*i+1`
We also create an empty queue to fill in the nodes(children) of next level while traversing the nodes at current level.

Following steps were used to solve the problem.
1. Traverse (BFS) through each node in level.
2. Add children of that level to `level_queue` object along with its `index`.
3. After the level traversal is complete and we have nodes for the next level, we look at the **right most** and **left most** node and subtract their indices and add 1 to get the width of the next level.
4. Then, we update `max_width` with `level_width` if it is greater and also update `queue` with `level_queue`.
5. Repeat 1 to 4 for the next level until queue is empty. 


# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
![image.png](https://assets.leetcode.com/users/images/d2082cf6-9275-49b9-9193-e43a20131a8b_1682025583.9748878.png)


- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create a queue with node and index
        queue = [(root, 0)]
        level_queue = queue
        max_width = 1
        while queue:
            level_queue = []
            # Loop through each node in the level frontier to get its child
            for node, i in queue:
                if node.left:
                    level_queue.append((node.left, 2*i+1))
                if node.right:
                    level_queue.append((node.right, 2*i+2))
            # Check the max width at the current level
            if level_queue:
                # We subtract the index of right most and the left most child
                # of that level to get level width
                level_width = level_queue[-1][1] - level_queue[0][1] + 1
                if level_width > max_width:
                    max_width = level_width
            # Replace the queue with child of next level
            queue = level_queue

        return max_width

```


