# 1015. Smallest Integer Divisible by K

<div align="center">

**🟡 MEDIUM** | **Tags:** `Math`, `Number Theory`, `Simulation`

</div>

---

## 📖 Problem Statement

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.  Return the length of n. If there is no such n, return -1.  Note: n may not fit in a 64-bit signed integer.     Example 1:  Input: k = 1 Output: 1 Explanation: The smallest answer is n = 1, which has length 1. Example 2:  Input: k = 2 Output: -1 Explanation: There is no such positive integer n divisible by 2. Example 3:  Input: k = 3 Output: 3 Explanation: The smallest answer is n = 111, which has length 3.    Constraints:  1 <= k <= 105

### Input Format
> A positive integer k.

### Output Format
> The length of the smallest positive integer n divisible by k and composed only of the digit 1. Return -1 if no such integer exists.

---

## 💡 Key Insight

The solution leverages the properties of modular arithmetic to efficiently find the smallest number composed solely of '1's that is divisible by k. It iteratively constructs numbers like 1, 11, 111, etc., by appending '1' and taking the remainder modulo k. If a remainder of 0 is found, the current length is the answer. Numbers divisible by 2 or 5 are impossible, hence the initial check.

---

## 🎯 Hints to Solve

> **Hint 1:** Consider the numbers formed by only '1's: 1, 11, 111, 1111, ...
> **Hint 2:** Notice the pattern: `n_i = n_{i-1} * 10 + 1`. This can be used with modular arithmetic.
> **Hint 3:** We are looking for `n % k == 0`. This is equivalent to `(n_{i-1} * 10 + 1) % k == 0`.
> **Hint 4:** The remainders when dividing by k will eventually repeat. If a remainder repeats before we find 0, then 0 will never be reached.
> **Hint 5:** If k is divisible by 2 or 5, no number consisting only of 1s can be divisible by k. Why?
> **Hint 6:** The maximum length we need to check is k, because by the Pigeonhole Principle, if we haven't found a solution by then, a remainder must have repeated.


---

## 🔍 Algorithm Overview

```
function smallestRepunitDivByK(k):
  // If k is divisible by 2 or 5, no such number exists.
  if k % 2 == 0 or k % 5 == 0:
    return -1

  // Initialize remainder and length.
  remainder = 0
  length = 0

  // Iterate up to k times (Pigeonhole Principle).
  for length from 1 to k:
    // Calculate the next number's remainder modulo k.
    // This is equivalent to (current_number * 10 + 1) % k
    remainder = (remainder * 10 + 1) % k

    // If the remainder is 0, we found a divisible number.
    if remainder == 0:
      return length

  // If no solution is found within k iterations, return -1.
  return -1
```

---

## 📋 Step-by-Step Approach

1. Handle the edge case where k is divisible by 2 or 5, returning -1 immediately.
2. Initialize a variable `remainder` to 0 and `length` to 0.
3. Iterate from `length = 1` up to `k`.
4. In each iteration, update the `remainder` using the formula: `remainder = (remainder * 10 + 1) % k`.
5. This formula simulates appending a '1' to the current number and taking the modulo k.
6. If at any point `remainder` becomes 0, it means the number formed by `length` ones is divisible by `k`. Return `length`.
7. If the loop completes without finding a `remainder` of 0, it implies no such number exists within the possible range. Return -1.


---

## 🚶 Detailed Walkthrough

Let's trace for k = 3:

Initial state: k = 3. k is not divisible by 2 or 5. remainder = 0, length = 0.

Iteration 1 (length = 1):
  remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1
  remainder is not 0.
  Current number conceptually: 1

Iteration 2 (length = 2):
  remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2
  remainder is not 0.
  Current number conceptually: 11

Iteration 3 (length = 3):
  remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0
  remainder is 0! We found a solution.
  Return length = 3.

Visual Representation:

k = 3

Length 1:  1   (1 % 3 = 1)
Length 2: 11   (11 % 3 = 2)
Length 3: 111  (111 % 3 = 0) -> Found!


Let's trace for k = 7:

Initial state: k = 7. k is not divisible by 2 or 5. remainder = 0, length = 0.

Iteration 1 (length = 1): remainder = (0*10 + 1) % 7 = 1
Iteration 2 (length = 2): remainder = (1*10 + 1) % 7 = 11 % 7 = 4
Iteration 3 (length = 3): remainder = (4*10 + 1) % 7 = 41 % 7 = 6
Iteration 4 (length = 4): remainder = (6*10 + 1) % 7 = 61 % 7 = 5
Iteration 5 (length = 5): remainder = (5*10 + 1) % 7 = 51 % 7 = 2
Iteration 6 (length = 6): remainder = (2*10 + 1) % 7 = 21 % 7 = 0 -> Found!
Return length = 6.

Visual Representation:

k = 7

Length 1:  1   (1 % 7 = 1)
Length 2: 11   (11 % 7 = 4)
Length 3: 111  (111 % 7 = 6)
Length 4: 1111 (1111 % 7 = 5)
Length 5: 11111(11111 % 7 = 2)
Length 6: 111111(111111 % 7 = 0) -> Found!


---

## 📊 Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time** | O(k) | O(k) - The loop iterates at most k times. In each iteration, we perform constant time arithmetic operations (multiplication, addition, modulo). Therefore, the time complexity is directly proportional to the value of k. |
| **Space** | O(1) | O(1) - The solution uses only a few variables (`k`, `remainder`, `length`) to store intermediate values. The amount of memory used does not grow with the input size k, making it constant space. |

---

## ⚠️ Edge Cases to Consider

- ✓ k = 1: The smallest number is 1, length is 1. The code handles this correctly as (0*10+1)%1 = 0, returning 1.
- ✓ k is even (e.g., k = 2, 4, 6): No number consisting only of 1s can be even. The initial check `k % 2 == 0` correctly returns -1.
- ✓ k is a multiple of 5 (e.g., k = 5, 10, 15): No number consisting only of 1s can end in 0 or 5. The initial check `k % 5 == 0` correctly returns -1.
- ✓ k is a prime number not 2 or 5 (e.g., k = 3, 7, 11, 13): These cases are handled by the main loop, and a solution is guaranteed to be found within k iterations due to the Pigeonhole Principle on remainders.


---

## 📥 Test Examples

### Example 1

| Type | Value |
|------|-------|
| **Input** | `k = 1` |
| **Output** | `1` |

### Example 2

| Type | Value |
|------|-------|
| **Input** | `k = 2` |
| **Output** | `-1` |

### Example 3

| Type | Value |
|------|-------|
| **Input** | `k = 3` |
| **Output** | `3` |

---

<div align="center">

**Generated:** 2025-11-27 15:36:54

---

*Keep learning, keep coding! 🚀*

</div>
