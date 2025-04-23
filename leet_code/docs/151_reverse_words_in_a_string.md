# Intuition
When I first looked at this problem, I realized that if I could reverse the entire string, the words would end up in the correct reversed order, but each word would be backwards. So, if I then reversed each word individually, the letters would be in the right order again. The only thing left would be to clean up any extra spaces (leading, trailing, or between words). This three-step process felt both simple and efficient.

# Approach
Here's how I tackled the problem:

1. **Reverse the whole string**:  
   By reversing all the characters, the last word comes to the front, but each word is reversed letter by letter.

2. **Reverse each word**:  
   I scan through the string, find each word, and reverse just that word so the letters are in the correct order again.

3. **Clean up spaces**:  
   Finally, I go through the string one more time to remove extra spaces. I use two pointers: one to read through the string, and one to write back only the necessary characters, making sure there are no leading or trailing spaces and only single spaces between words.

# Complexity
- Time complexity:  
  $$O(n)$$  
  Every character is visited a constant number of times—once for each of the three main steps.

- Space complexity:  
  $$O(1)$$  
  All operations are done in-place on the character list (ignoring the output string required by the function signature).

# Code
```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to list for in-place modification since strings are immutable
        s = list(s)
        n = len(s)

        # Helper function to reverse characters in s between indices left and right inclusive
        def reverse_string(s, left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire string
        # This puts the words in reverse order, but each word itself is reversed
        reverse_string(s, 0, n - 1)

        # Step 2: Reverse each word individually to restore correct word order
        # head will scan through the list to find word boundaries
        head = 0
        while head < n:
            # Skip any spaces to find the start of a word
            while head < n and s[head] == ' ':
                head += 1
            # tail will find the end of the current word
            tail = head
            while tail < n and s[tail] != ' ':
                tail += 1
            # Reverse the current word to restore its correct order
            reverse_string(s, head, tail - 1)
            # Move head to the end of the current word to continue scanning
            head = tail

        # Step 3: Clean up spaces in-place
        # Use two pointers:
        #   tail - reads through the list
        #   head - writes the cleaned characters back into the list
        head = 0  # write index
        tail = 0  # read index
        while tail < n:
            # Skip spaces to find the start of the next word
            while tail < n and s[tail] == ' ':
                tail += 1
            # Copy the characters of the current word
            while tail < n and s[tail] != ' ':
                s[head] = s[tail]
                head += 1
                tail += 1
            # After copying a word, check if there is another word ahead
            # If yes, insert a single space to separate words
            temp = tail
            while temp < n and s[temp] == ' ':
                temp += 1
            if temp < n:
                s[head] = ' '
                head += 1

        # Finally, join the characters up to head index to form the cleaned reversed string
        return ''.join(s[:head])
```