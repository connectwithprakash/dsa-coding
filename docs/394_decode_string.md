# Intuition
The idea is to find the string in the order of the `big brackets` and multiply the string by the number preceeding the bracket.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
We loop through the string `s` and handle the situation according to character seen.
1. If the character is an `opening bracket` then recurse through the rest of the string. 
2. If the character is `closing bracket` then break out of recursion. 
3. If the character is `numeric` then store it in repeat string.
4. If the character is `alpha` then store it in result and use `repeat` to repeat the string by multiply it with repeat value.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
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

```

