class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p, q = 0, len(s)
        def recursive(p, q):
            if (q-p) == 1:
                return 1
            mid = (p+q)//2
            left_len = recursive(p, mid)
            right_len = recursive(mid, q)
            # Swap left and right half
            s[p:p+right_len], s[q-left_len:q] = s[mid:q], s[p:mid]

            return (q-p)

        recursive(p, q)

        return s
  
