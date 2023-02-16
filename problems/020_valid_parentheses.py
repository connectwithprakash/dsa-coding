class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
                    '(': ')',
                    '{': '}',
                    '[': ']'
                    }
        stack = []
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif (len(stack) == 0) or (stack.pop() != c):
                return False
        if len(stack):
            return False
        else:
            return True


if __name__ == "__main__":
    assert (Solution().isValid("]") == False)
    assert (Solution().isValid("[") == False)
    assert (Solution().isValid("()") == True)
    assert (Solution().isValid("()[]{}") == True)
    assert (Solution().isValid('{]') == False)
    assert (Solution().isValid('[{(){[]()}}]') == True)

