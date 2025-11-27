# 1015. Smallest Integer Divisible by K

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Math`, `Number Theory`, `Simulation`

---

## 📝 Problem Statement

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.  Return the length of n. If there is no such n, return -1.  Note: n may not fit in a 64-bit signed integer.     Example 1:  Input: k = 1 Output: 1 Explanation: The smallest answer is n = 1, which has length 1. Example 2:  Input: k = 2 Output: -1 Explanation: There is no such positive integer n divisible by 2. Example 3:  Input: k = 3 Output: 3 Explanation: The smallest answer is n = 111, which has length 3.    Constraints:  1 <= k <= 105

### Input
A positive integer k.

### Output
The length of the smallest positive integer n divisible by k and consisting only of the digit 1. Return -1 if no such n exists.

---

## 💡 Explanation

The solution iteratively constructs numbers consisting only of the digit '1' (1, 11, 111, ...) and checks their divisibility by `k`. It leverages the **modulo operator** to efficiently track the remainder without needing to store the large numbers themselves. If a remainder of 0 is found, the current length is the answer. If `k` is divisible by 2 or 5, no such number exists, and -1 is returned.

---

## 🎯 Hints

1. Consider the properties of numbers formed solely by the digit '1'.
2. Think about how to represent and check divisibility of potentially very large numbers efficiently.
3. The **remainder** when dividing by `k` is crucial. How does it change when appending a '1'?
4. If `k` is even or a multiple of 5, can a number composed only of '1's ever be divisible by `k`?
5. What is the maximum possible length of the smallest repunit divisible by `k`?
6. Use the **Pigeonhole Principle** to understand why a solution must exist within a certain number of steps if `k` is not divisible by 2 or 5.

---

## 🔍 Algorithm

```
function smallestRepunitDivByK(k):
  if k is divisible by 2 or k is divisible by 5:
    return -1

  remainder = 0
  for length from 1 to k:
    remainder = (remainder * 10 + 1) % k
    if remainder is 0:
      return length

  return -1
```

---

## 📋 Approach

1. Handle the **edge case** where `k` is divisible by 2 or 5. In such cases, no number composed solely of '1's can be divisible by `k`, so return -1.
2. Initialize a variable `remainder` to 0. This will store the remainder of the current repunit number when divided by `k`.
3. Iterate through possible lengths of the repunit number, starting from 1 up to `k`. The maximum length needed is `k` due to the Pigeonhole Principle.
4. In each iteration, update the `remainder`. The new repunit number is formed by taking the previous one, multiplying it by 10, and adding 1. The remainder of this new number when divided by `k` can be calculated as `(previous_remainder * 10 + 1) % k`.
5. Check if the `remainder` becomes 0. If it does, it means the current repunit number (with the current `length`) is divisible by `k`. Return the `length`.
6. If the loop completes without finding a remainder of 0, it implies no such number exists within the considered range (though this case is covered by the initial check for divisibility by 2 or 5). Return -1.

---

## 🚶 Step-by-Step Walkthrough

Let's trace for k = 3:

Initial state: k = 3. k is not divisible by 2 or 5.
remainder = 0

Iteration 1 (length = 1):
  remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1
  remainder is not 0.

Iteration 2 (length = 2):
  remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2
  remainder is not 0.

Iteration 3 (length = 3):
  remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0
  remainder is 0! Return length = 3.


Let's trace for k = 2:

Initial state: k = 2. k is divisible by 2.
Return -1.


Let's trace for k = 7:

Initial state: k = 7. k is not divisible by 2 or 5.
remainder = 0

Iteration 1 (length = 1):
  remainder = (0 * 10 + 1) % 7 = 1 % 7 = 1

Iteration 2 (length = 2):
  remainder = (1 * 10 + 1) % 7 = 11 % 7 = 4

Iteration 3 (length = 3):
  remainder = (4 * 10 + 1) % 7 = 41 % 7 = 6

Iteration 4 (length = 4):
  remainder = (6 * 10 + 1) % 7 = 61 % 7 = 5

Iteration 5 (length = 5):
  remainder = (5 * 10 + 1) % 7 = 51 % 7 = 2

Iteration 6 (length = 6):
  remainder = (2 * 10 + 1) % 7 = 21 % 7 = 0
  remainder is 0! Return length = 6.
  (The number is 111111, which is 111111 / 7 = 15873)

---

## 📊 Complexity Analysis

### Time Complexity
**O(k)** - The loop iterates at most `k` times. In each iteration, we perform constant time arithmetic operations (multiplication, addition, modulo). Therefore, the time complexity is directly proportional to `k`.

### Space Complexity
**O(1)** - The solution uses only a few variables (`k`, `remainder`, `length`) to store intermediate values. The amount of memory used does not grow with the input `k`.

---

## ⚠️ Edge Cases

- k = 1: The smallest repunit is 1, length is 1.
- k is even (e.g., k = 2, k = 4, k = 6): No solution exists, return -1.
- k is a multiple of 5 (e.g., k = 5, k = 10, k = 15): No solution exists, return -1.
- k is a prime number not divisible by 2 or 5 (e.g., k = 3, k = 7, k = 11): A solution will always exist within `k` iterations.

---

## 📥 Examples

### Example 1
**Input:** `k = 1`
**Output:** `1`

### Example 2
**Input:** `k = 2`
**Output:** `-1`

### Example 3
**Input:** `k = 3`
**Output:** `3`

---
*Generated on 2025-11-27 16:14:18*
