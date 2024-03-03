class Solution:
    def decodeString(self, s: str) -> str:
        def recursion(index):
            result = []
            repeat = ""
            while index < len(s):
                if (s[index] == '['):
                    index, rec_result = recursion(index+1)
                    result += (rec_result *int(repeat))
                    repeat = ""
                elif (s[index] == ']'):
                    return index, result
                else:
                    if s[index].isalpha():
                        result.append(s[index])
                    else:
                        repeat += s[index]
                
                index += 1

            return index, result

        _, result = recursion(0)

        return "".join(result)

