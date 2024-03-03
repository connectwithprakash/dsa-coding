# Attempt 1: Bruteforce solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            diff = stones[-1] - stones[-2]
            stones = stones[:-2]
            stones.append(diff)

        return stones[0]


# Attempt 2: Using heap
# O(n) space and time complexity solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            diff = heapq.heappop(heap) - heapq.heappop(heap)
            if (diff < 0):
                heapq.heappush(heap, diff)

        if len(heap):
            return -heap[0]
        else:
            return 0


# Attempt 3: Using heap
# O(n) time complexity and O(1) space complexity solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            if (diff < 0):
                heapq.heappush(stones, diff)

        if len(stones):
            return -stones[0]
        else:
            return 0
