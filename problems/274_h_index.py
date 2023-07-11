class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_h = len(citations)
        for h in range(max_h, 0, -1):
            count = 0
            for citation in citations:
                if citation >= h:
                    count += 1
            if count >= h:
                break

        return min(count, h)

