class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            if popped[j] == pushed[i]:
                stack.pop()
                j += 1

        for i in range(j, len(popped)):
            if stack.pop() != popped[i]:
                return False

        return True

