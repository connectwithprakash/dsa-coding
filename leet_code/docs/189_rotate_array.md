# Intuition
![189_rotate_array_scratch_pad.PNG](https://assets.leetcode.com/users/images/166c58b7-1e3f-4a03-8f9e-2e09c24288e4_1687227038.680077.png)

After working through examples with different values of "k" following the k numbers from last. We iteratively swap the number from kth from last to nth with its respective new index. After than we see that the numbers from 0th to k-1th index from last needs some rotation to fix their placements because they could get mixed up. So, we do the same k times rotation of the remaining numbers.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
**offset:** We define offset variable to store the number of rotations done. We use this vaibale to compute total remaining numbers that needs rotations. Also, the same variable is used to define the index to swap the number with i.e. the new position of last k numbers.

**swap_idx:** This variable computes the new index for the number being swapped for rotation.

## Algorithm
1. Loop through the numbers untill rotation is complete. The rotation is complete if there are 'k' numbers (left) and 'k' rotations required.
2. Iterate i through the last kth to nth elements.
    2.1. Create a new index to swap ith element. Offset shift index to rotate through array.
3. Increment offset by the value of k. This segregates the already rotated elements from last kth to nth element and the remaining rotated (wrongly) elements.



# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        offset = 0
        n = len(nums)
        while True:
            k = k % (n - offset)
            if k == 0:
                break
            for i in range(n-k, n):
                swap_i = ((i + k) % n) + offset
                nums[swap_i], nums[i] = nums[i], nums[swap_i]
            offset += k

```

