class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in decending order
        citations.sort(reverse=True)
        # find the maximum x >= y point on the x=y line
        h_index = 0
        for citation in citations:
            if citation > h_index:
               h_index += 1
            else:
                break

        return h_index

