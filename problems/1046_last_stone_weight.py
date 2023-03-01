class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            diff = stones[-1] - stones[-2]
            stones = stones[:-2]
            stones.append(diff)
            
        return stones[0]

