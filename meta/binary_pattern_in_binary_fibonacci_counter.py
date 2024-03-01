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


