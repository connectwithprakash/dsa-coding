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


# Attempt 2: Using Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                match token:
                    case '+':
                        result = operand1 + operand2
                    case '-':
                        result = operand1 - operand2
                    case '*':
                        result = operand1 * operand2
                    case '/':
                        result = int(operand1 / operand2)
                stack.append(result)                        
            else:
                stack.append(int(token))

        return stack[0]

