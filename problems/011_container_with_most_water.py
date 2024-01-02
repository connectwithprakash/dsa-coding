class Solution:
    def maxArea(self, height: List[int]) -> int:
        idx, jdx = 0, len(height)-1
        max_water = 0
        while idx < jdx:
            water = min(height[idx], height[jdx])*(jdx-idx)
            if water > max_water:
                max_water = water
            # Move the the pointer with lower height
            if height[idx] < height[jdx]:
                idx += 1
            else:
                jdx -= 1

        return max_water

