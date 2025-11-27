# 1015. Smallest Integer Divisible by K

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Math`, `Number Theory`, `Simulation`

---

## 📝 Problem Statement

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.  Return the length of n. If there is no such n, return -1.  Note: n may not fit in a 64-bit signed integer.     Example 1:  Input: k = 1 Output: 1 Explanation: The smallest answer is n = 1, which has length 1. Example 2:  Input: k = 2 Output: -1 Explanation: There is no such positive integer n divisible by 2. Example 3:  Input: k = 3 Output: 3 Explanation: The smallest answer is n = 111, which has length 3.    Constraints:  1 <= k <= 105

### Input
A positive integer k.

### Output
The length of the smallest positive integer n divisible by k and composed only of the digit 1. Return -1 if no such integer exists.

---

## 💡 Explanation

The solution leverages the property of modular arithmetic to efficiently find the smallest number composed solely of '1's that is divisible by `k`. It iteratively constructs numbers of the form 1, 11, 111, ... and checks their remainders when divided by `k`. If a remainder of 0 is found, the current length is the answer. This avoids dealing with potentially massive numbers by only tracking the remainder.

---

## 🎯 Hints

1. Consider the numbers formed by only the digit '1': 1, 11, 111, 1111, ...
2. Notice the pattern: `11...1` (length `L`) can be expressed as `(11...1 (length L-1)) * 10 + 1`.
3. Instead of calculating the full number, focus on its **remainder** when divided by `k`.
4. The problem guarantees that if a solution exists, it will be found within `k` iterations. Why?
5. Think about the possible remainders when dividing by `k`. There are only `k` possible remainders (0 to k-1).
6. If `k` is divisible by 2 or 5, no such number composed of only '1's can exist. Why?

---

## 🔍 Algorithm

```
function smallestRepunitDivByK(k):
  // Handle impossible cases: k divisible by 2 or 5
  if k % 2 == 0 or k % 5 == 0:
    return -1

  // Initialize remainder and length
  remainder = 0
  length = 0

  // Iterate up to k times (Pigeonhole Principle)
  for length from 1 to k:
    // Calculate the next repunit number's remainder
    // The current number is `remainder * 10 + 1`
    remainder = (remainder * 10 + 1) % k

    // If remainder is 0, we found the smallest repunit divisible by k
    if remainder == 0:
      return length

  // If loop finishes without finding a solution (should not happen for valid k)
  return -1
```

---

## 📋 Approach

1. **Check for impossible cases**: If `k` is divisible by 2 or 5, return -1 immediately, as any number formed only by '1's will always end in '1' and thus be odd and not divisible by 5.
2. **Initialize variables**: Set `remainder` to 0 and `length` to 0.
3. **Iterate and calculate remainders**: Loop from `length = 1` up to `k`. In each iteration, calculate the remainder of the next repunit number (formed by appending a '1') when divided by `k`. This is done using the formula `(current_remainder * 10 + 1) % k`.
4. **Check for divisibility**: Inside the loop, if the calculated `remainder` becomes 0, it means the current repunit number is divisible by `k`. Return the current `length`.
5. **Handle no solution**: If the loop completes without finding a remainder of 0, return -1 (though this scenario is theoretically impossible for valid `k` due to the Pigeonhole Principle).

---

## 🚶 Step-by-Step Walkthrough

Let's trace for k = 3:

Initial state: k = 3, remainder = 0, length = 0

Iteration 1 (length = 1):
  remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1
  remainder is not 0.

Iteration 2 (length = 2):
  remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2
  remainder is not 0.

Iteration 3 (length = 3):
  remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0
  remainder is 0! Return length = 3.

Smallest repunit divisible by 3 is 111, which has length 3.


Let's trace for k = 7:

Initial state: k = 7, remainder = 0, length = 0

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

Smallest repunit divisible by 7 is 111111, which has length 6.

---

## 📊 Complexity Analysis

### Time Complexity
The loop runs at most `k` times. Inside the loop, operations are constant time (multiplication, addition, modulo). Therefore, the time complexity is **O(k)**.

### Space Complexity
The solution only uses a few variables (`k`, `remainder`, `length`) to store intermediate values. The space used does not grow with the input `k`. Therefore, the space complexity is **O(1)**.

---

## ⚠️ Edge Cases

- k = 1: The smallest repunit is 1, length is 1.
- k is divisible by 2 (e.g., k = 2, 4, 6): No solution exists, return -1.
- k is divisible by 5 (e.g., k = 5, 10, 15): No solution exists, return -1.
- k is a prime number (e.g., k = 3, 7, 11): The algorithm will find a solution.
- k is a large number within the constraint (e.g., k = 100000): The algorithm will still perform efficiently due to the O(k) time complexity.

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
*Generated on 2025-11-27 17:23:20*
