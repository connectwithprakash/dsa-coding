# Binary Fibonacci Sequence Pattern Counter

This script allows you to count the occurrences of a binary pattern in the binary Fibonacci sequence using various methods.

## Problem Description

In this problem, binary Fibonacci means the concatenation of binary bits as follows:

```
f(0) = 0
f(1) = 1
f(2) = f(1) + f(0) = 10
f(3) = f(2) + f(1) = 101
f(4) = f(3) + f(2) = 10110
f(5) = f(4) + f(3) = 10110101
f(6) = f(5) + f(4) = 1011010110110
...
```

Given a binary pattern, you need to count the number of occurrences of the pattern in the binary Fibonacci sequence.

### Example

**Input:**

```
pattern = 10
n = 6
```

**Output:**

```
5
```

**Explanation:**

The binary Fibonacci sequence is:

```
f(6) = 1011010110110
10_1_10_10_1_10_1_10
```

The pattern `10` occurs 5 times in the sequence. (1-2, 4-5, 6-7, 9-10, 12-13)

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Methods](#methods)
- [Testing](#testing)

## Description

The script consists of functions and a class designed to work with the binary Fibonacci sequence. It offers methods to count the occurrences of a given binary pattern within the binary Fibonacci sequence using different techniques such as string matching, logical operations, and observing patterns in the counts of Fibonacci numbers.

## Features

- Conversion functions to convert binary numbers to decimal and vice versa.
- Calculation of the binary Fibonacci sequence.
- Methods to count binary pattern occurrences using string matching, logical operations, and pattern observation.
- Testing functions to ensure script functionality.

## Usage

To use the script, simply import it into your Python environment. Here's a basic example:

```python
from binary_fibonacci_counter import Solution

# Create an instance of the Solution class
solution = Solution()

# Count occurrences of a binary pattern in the binary Fibonacci sequence
count = solution.count_binary_pattern("10", 6)
print("Occurrences:", count)
```

## Methods

- `count_using_string_matching(pattern: str, n: int) -> int`: Counts occurrences of a binary pattern using string matching.
- `count_using_logical_operations(pattern: str, n: int) -> int`: Counts occurrences of a binary pattern using logical operations.
- `count_following_pattern_in_count_sequence(pattern: str, n: int) -> int`: Counts occurrences of a binary pattern by observing patterns in Fibonacci number counts.
- `count_binary_pattern_occurences_in_binary_fibonacci(pattern: str, n: int) -> Dict[str, int]`: Counts occurrences of a binary pattern using multiple methods and returns counts.
- `count_binary_pattern(pattern: str, n: int) -> int`: Counts occurrences of a binary pattern up to a given index.
- `count_binary_pattern_upto_n(pattern: str, n: int) -> Dict[int, int]`: Counts occurrences of a binary pattern up to each index up to n.

## Testing

The script includes testing functions to ensure its functionality. You can run the tests by executing the script directly:

```
python binary_fibonacci_counter.py
```
