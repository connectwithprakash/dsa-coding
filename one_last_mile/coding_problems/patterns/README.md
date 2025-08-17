# Pattern Recognition Guide for Coding Problems

## Overview
This guide helps identify which algorithmic pattern to apply based on problem characteristics. After solving 27+ problems, I've identified key patterns that repeatedly appear in technical interviews.

## Quick Pattern Selection Decision Tree

```
Start Here
    ↓
Is the input sorted or can be sorted?
    YES → Consider Two Pointers or Binary Search
    NO ↓
    
Does problem involve substring/subarray?
    YES → Consider Sliding Window
    NO ↓
    
Need to find "next greater/smaller" element?
    YES → Use Monotonic Stack
    NO ↓
    
Need to track frequencies or counts?
    YES → Use HashMap/Frequency Counting
    NO ↓
    
Need cumulative information?
    YES → Consider Prefix/Suffix patterns
    NO ↓
    
Need to track min/max efficiently?
    YES → Consider Heap or Monotonic Structure
```

## Core Patterns

### 1. [Monotonic Stack](./monotonic_stack.md)
**When to use**: Finding next greater/smaller element, maintaining order
**Key problems**: Daily Temperatures, Largest Rectangle in Histogram
**Complexity**: Usually O(n) - each element pushed/popped once

### 2. [Sliding Window](./sliding_window.md)
**When to use**: Substring/subarray problems with consecutive elements
**Key problems**: Longest Substring Without Repeating, Minimum Window Substring
**Complexity**: O(n) for single pass, sometimes O(n²) for nested operations

### 3. [Two Pointers](./two_pointers.md)
**When to use**: Sorted arrays, palindromes, optimization problems
**Key problems**: 3Sum, Container With Most Water, Trapping Rain Water
**Complexity**: O(n) for single pass, O(n²) if nested

### 4. [Frequency Counting](./frequency_counting.md)
**When to use**: Anagrams, top k elements, character/element counts
**Key problems**: Valid Anagram, Group Anagrams, Top K Frequent Elements
**Complexity**: O(n) for counting, varies for processing

### 5. [Prefix/Suffix](./prefix_suffix.md)
**When to use**: Need cumulative information from both directions
**Key problems**: Product of Array Except Self, Trapping Rain Water
**Complexity**: O(n) with O(n) or O(1) space

## Pattern Recognition Keywords

| Keywords/Phrases | Likely Pattern |
|-----------------|----------------|
| "next greater/smaller" | Monotonic Stack |
| "substring with condition" | Sliding Window |
| "longest/shortest substring" | Sliding Window |
| "sorted array" | Two Pointers or Binary Search |
| "palindrome" | Two Pointers |
| "top/bottom k elements" | Heap or Bucket Sort |
| "frequency", "count occurrences" | HashMap/Frequency Counting |
| "anagram", "permutation" | Frequency Counting |
| "cumulative", "product except self" | Prefix/Suffix |
| "valid parentheses" | Stack |
| "maximum area/water" | Two Pointers or Stack |

## Common Pattern Combinations

### Sliding Window + Frequency Counting
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring

### Stack + Greedy
- Valid Parentheses
- Generate Parentheses

### Two Pointers + Greedy
- Container With Most Water
- Trapping Rain Water

### Monotonic Stack + Index Tracking
- Largest Rectangle in Histogram
- Daily Temperatures

## Problem-Solving Approach

1. **Identify constraints**: Array sorted? Only lowercase letters? Non-negative?
2. **Look for keywords**: Check the pattern recognition table above
3. **Consider brute force**: What's the naive approach?
4. **Optimize with patterns**: Which pattern reduces complexity?
5. **Handle edge cases**: Empty input, single element, all same elements

## Quick Reference Links

- [Problem-Pattern Mapping](./problem_pattern_map.md) - See which problems use which patterns
- [Pattern Triggers](./pattern_triggers.md) - Detailed keyword analysis
- [Complexity Patterns](./complexity_patterns.md) - Common complexity formulas

## Tips for Pattern Mastery

1. **Start with the pattern template** - Each pattern has a basic structure
2. **Modify for specific requirements** - Adapt the template to problem needs
3. **Combine patterns when needed** - Many problems use 2+ patterns
4. **Practice pattern recognition** - The more you solve, the faster you recognize
5. **Understand why it works** - Don't just memorize, understand the logic

## My Learning Journey

After solving problems across different categories, I've noticed that recognizing patterns is more important than memorizing solutions. Each pattern document includes:
- Problems I've solved using that pattern
- My thought process for recognizing the pattern
- Common variations and edge cases
- Evolution from brute force to optimal solution