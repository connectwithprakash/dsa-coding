class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Get lengths of input strings
        len_a, len_b = len(a), len(b)
        min_len = min(len_a, len_b)

        # Ensure 'a' is always the longer string for simpler processing
        if len_a == min_len:
            a, b = b, a
            len_a, len_b = len_b, len_a

        carry = False  # Track carry bit
        result = []  # Store result digits

        # Process digits from right to left for the length of shorter string
        for idx in range(min_len):
            # Get current digits from right to left
            digit_a = a[len_a - idx - 1]
            digit_b = b[len_b - idx - 1]

            # Case 1: Both digits are 1
            if digit_a == "1" and digit_b == "1":
                # If carry exists: 1 + 1 + 1 = 11 (append 1, carry stays 1)
                # If no carry: 1 + 1 = 10 (append 0, carry becomes 1)
                result.append("1" if carry else "0")
                carry = True

            # Case 2: Both digits are 0
            elif digit_a == "0" and digit_b == "0":
                # If carry exists: 0 + 0 + 1 = 1 (append 1, carry becomes 0)
                # If no carry: 0 + 0 = 0 (append 0, carry stays 0)
                result.append("1" if carry else "0")
                carry = False

            # Case 3: One digit is 1, other is 0
            else:
                # If carry exists: 1 + 0 + 1 = 10 (append 0, carry stays 1)
                # If no carry: 1 + 0 = 1 (append 1, carry stays 0)
                result.append("0" if carry else "1")

        # Process remaining digits of longer string 'a'
        idx = min_len
        while idx < len_a:
            digit = a[len_a - idx - 1]
            if carry:
                if digit == "1":
                    # 1 + 1 = 10 (append 0, carry stays 1)
                    result.append("0")
                    carry = True
                else:
                    # 0 + 1 = 1 (append 1, carry becomes 0)
                    result.append("1")
                    carry = False
            else:
                # No carry, just append the digit as is
                result.append(digit)
            idx += 1

        # If there's still a carry after processing all digits
        # add it as the most significant bit
        if carry:
            result.append("1")

        # Reverse the result and join into a string
        # We built the result from right to left, so we need to reverse it
        return "".join(result[::-1])
