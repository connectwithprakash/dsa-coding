# Brute-force solution
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        j = 0
        for i in range(n):
            stack.append(pushed[i])
            while (j < n):
                if (popped[j] in stack):
                    stack.pop()
                    j += 1
                else:
                    break

        for i in range(j, n):
            if stack.pop() != popped[i]:
                return False

        return True            

