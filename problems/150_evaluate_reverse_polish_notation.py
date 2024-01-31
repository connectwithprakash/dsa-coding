# Attempt 1: Naive approach
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        idx = 0
        while len(tokens) > 1:
            if tokens[idx] in ['+', '-', '*', '/']:
                rev_pol_operation = tokens[idx-2]+tokens[idx]+tokens[idx-1]
                tokens[idx] = str(int(eval(rev_pol_operation)))
                tokens = tokens[:idx-2]+tokens[idx:]
                idx -= 2
            else:
                idx += 1
        return int(tokens[0])

