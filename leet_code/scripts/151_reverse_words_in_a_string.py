# Attempt 1: Pythonic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n) space complexity approach
        # n = len(s)
        # jdx = 0
        # start_word = False
        # res_s = ''
        # for idx in range(n-1, -1, -1):
        #     if not start_word and s[idx] != ' ':
        #         start_word = True
        #         jdx = idx+1

        #     if start_word:
        #         if s[idx] == ' ':
        #             start_word = False
        #             res_s += s[idx+1:jdx] + ' '
        #         elif idx == 0:
        #             start_word = False
        #             res_s += s[:jdx] + ' '

        # return res_s[:-1]

        # O(1) space complexity
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
            while head < n and s[head] == " ":
                head += 1
            # tail will find the end of the current word
            tail = head
            while tail < n and s[tail] != " ":
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
            while tail < n and s[tail] == " ":
                tail += 1
            # Copy the characters of the current word
            while tail < n and s[tail] != " ":
                s[head] = s[tail]
                head += 1
                tail += 1
            # After copying a word, check if there is another word ahead
            # If yes, insert a single space to separate words
            temp = tail
            while temp < n and s[temp] == " ":
                temp += 1
            if temp < n:
                s[head] = " "
                head += 1

        # Finally, join the characters up to head index to form the cleaned reversed string
        return "".join(s[:head])
