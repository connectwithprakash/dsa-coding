# Brute-force solution: O(n^2) because of the search statement in if condition
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


# Efficient solution: O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and (j < n):
                if (stack[-1] == popped[j]):
                    stack.pop()
                    j += 1
                else:
                    break

        return len(stack) == 0         


# Efficient solution 2: O(n) space and time complexity
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        for x in pushed:
            pushed[i] = x
            while (i > -1) and (pushed[i] == popped[j]):
                i -= 1
                j += 1
            i += 1

        return (i == 0)

