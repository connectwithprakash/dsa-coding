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
