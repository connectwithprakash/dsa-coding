class Solution:
    def decodeString(self, s: str) -> str:
        def recursion(index):
            repeats = []
            result = []
            while index < len(s):
                if (s[index] == '['):
                    repeat = result.pop()
                    index, rec_result = recursion(index+1)
                    rec_result *= eval(repeat)
                    result += rec_result
                elif (s[index] == ']'):
                    return index, result
                else:
                    result.append(s[index])

                index += 1

            return index, result

        _, result = recursion(0)

        return "".join(result)

