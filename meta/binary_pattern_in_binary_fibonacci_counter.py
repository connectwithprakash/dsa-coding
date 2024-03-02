"""
Counts the occurrences of a binary pattern in the binary Fibonacci sequence.

In this problem binary fibonacci means the concatenation of binary bits like following:

f(0) = 0
f(1) = 1
f(2) = f(1) + f(0) = 10
f(3) = f(2) + f(1) = 101
f(4) = f(3) + f(2) = 10110
f(5) = f(4) + f(3) = 10110101
f(6) = f(5) + f(4) = 1011010110110
...

Given a binary pattern, you need to count the number of occurences of the pattern in the binary fibonacci sequence.

Input:
pattern = 10
n = 6

Output:
5

Explanation:
The binary fibonacci sequence is:
f(6) = 1011010110110
10_1_10_10_1_10_1_10
The pattern 10 occurs 5 times in the sequence. (1-2, 4-5, 6-7, 9-10, 12-13)
"""

from typing import Union, Dict


def bin_to_dec(n: Union[str, int]) -> int:
    """
    Converts a binary number to its decimal representation.

    Args:
    - n: A binary number (either as a string or an integer).

    Returns:
    - int: The decimal representation of the binary number.
    """
    assert isinstance(n, str) or isinstance(
        n, int), "Input must be a string or an integer!"
    dec = 0
    for i, bit in enumerate(reversed(str(n))):
        dec += int(bit) * (2 ** i)
    return dec


def no_of_bits(n: int) -> int:
    """
    Determines the number of bits required to represent an integer.

    Args:
    - n: An integer.

    Returns:
    - int: The number of bits required to represent the integer.
    """
    assert isinstance(n, int), "Input must be an integer!"
    if n == 0:
        return 1
    return n.bit_length()


def num2bin(n: int) -> str:
    """
    Converts an integer to its binary representation.

    Args:
    - n: An integer.

    Returns:
    - str: The binary representation of the integer.
    """
    return bin(n)[2:]


def binary_fibonacci(n: int) -> int:
    """
    Calculates the binary Fibonacci number at a given index.

    Args:
    - n: An index for the binary Fibonacci sequence.

    Returns:
    - int: The binary Fibonacci number at the specified index.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    fn_2, fn_1 = 0, 1
    for _ in range(2, n+1):
        bit_len = no_of_bits(fn_2)
        fn = (fn_1 << bit_len) | fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn


class Solution:
    @staticmethod
    def count_using_string_matching(pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence using string matching.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        fib_n = binary_fibonacci(n)
        pattern_num = bin_to_dec(pattern)
        n_bin = num2bin(fib_n)
        pattern_bin = num2bin(pattern_num)
        pattern_len = len(pattern_bin)
        n_bin_len = len(n_bin)

        count = 0
        for idx in range(n_bin_len - pattern_len + 1):
            # Check if the substring matches the pattern
            if n_bin[idx:idx+pattern_len] == pattern_bin:
                count += 1
            idx += 1

        return count

    @staticmethod
    def count_using_logical_operations(pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence using logical operations.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        n_fib = binary_fibonacci(n)
        pattern_num = bin_to_dec(pattern)
        pattern_len = no_of_bits(pattern_num)
        n_len = no_of_bits(n_fib)

        pattern_mask = (1 << pattern_len) - 1
        shifted_n_fib = n_fib << 1
        count = 0

        for _ in range(n_len - pattern_len + 1):
            shifted_n_fib >>= 1
            masked_n_fib = shifted_n_fib & pattern_mask
            if masked_n_fib == pattern_num:
                count += 1

        return count

