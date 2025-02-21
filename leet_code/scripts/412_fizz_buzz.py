"""
Input: An integer value
Output: Output is an array, and contains Fizz, Buzz, FizzBuzz or string representation of the integer value depending of the logic.
Idea: A simple idea would be to check if the number is divisible by 3 and 5 and create a resulting string depending on that
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for idx in range(1, n + 1):
            idx_result = ""

            if idx % 3 == 0:
                idx_result += "Fizz"
            if idx % 5 == 0:
                idx_result += "Buzz"
            if len(idx_result) == 0:
                idx_result += str(idx)

            output.append(idx_result)

        return output
