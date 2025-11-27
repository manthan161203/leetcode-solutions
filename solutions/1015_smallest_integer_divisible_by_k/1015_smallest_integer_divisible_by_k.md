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

The solution leverages the property of modular arithmetic to efficiently find the smallest number composed solely of '1's that is divisible by k. It iteratively constructs numbers like 1, 11, 111, etc., by appending a '1' and taking the remainder modulo k at each step. If the remainder becomes 0, the current length is the answer. Numbers divisible by 2 or 5 are impossible, hence the initial check.

---

## 🎯 Hints

1. Consider the numbers formed by only digit '1': 1, 11, 111, 1111, ...
2. Notice the pattern: the next number is formed by (previous_number * 10 + 1).
3. We are looking for a number 'n' such that n % k == 0. This is equivalent to (n % k) == 0.
4. Instead of calculating large numbers, we can work with their **remainders** modulo k.
5. The problem guarantees that if a solution exists, it will be found within k iterations due to the **Pigeonhole Principle** on remainders.
6. Numbers divisible by 2 or 5 will never be formed solely by '1's, as they must end in an even digit or 0.

---

## 🔍 Algorithm

```
function smallestRepunitDivByK(k):
  // If k is divisible by 2 or 5, no such number exists.
  if k % 2 == 0 or k % 5 == 0:
    return -1

  // Initialize the remainder to 0.
  remainder = 0

  // Iterate from length 1 up to k.
  // The maximum possible length is k due to the Pigeonhole Principle.
  for length from 1 to k:
    // Calculate the next remainder: (previous_remainder * 10 + 1) % k
    // This simulates appending a '1' to the current repunit and taking modulo k.
    remainder = (remainder * 10 + 1) % k

    // If the remainder is 0, we have found a repunit divisible by k.
    if remainder == 0:
      return length

  // If the loop completes without finding a remainder of 0, no such number exists.
  // This case should ideally not be reached if k is not divisible by 2 or 5,
  // but it's a safeguard.
  return -1
```

---

## 📋 Approach

1. Check if k is divisible by 2 or 5. If so, return -1 immediately, as no number consisting only of '1's can be divisible by them.
2. Initialize a variable `remainder` to 0. This will store the remainder of the current repunit number when divided by k.
3. Iterate through possible lengths of the repunit number, starting from 1. The loop should run at most k times.
4. In each iteration, update the `remainder` using the formula: `remainder = (remainder * 10 + 1) % k`. This simulates building the next repunit (e.g., from 1 to 11, 11 to 111) and calculating its remainder modulo k.
5. If at any point the `remainder` becomes 0, it means the current repunit number is divisible by k. Return the current length.
6. If the loop finishes without finding a remainder of 0 (which should not happen for valid k based on the Pigeonhole Principle), return -1.

---

## 🚶 Step-by-Step Walkthrough

Let's walk through with k = 3:

Initial state: k = 3. k is not divisible by 2 or 5. remainder = 0.

Iteration 1 (length = 1):
  remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1
  remainder is not 0.
  Current repunit conceptually: 1

Iteration 2 (length = 2):
  remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2
  remainder is not 0.
  Current repunit conceptually: 11

Iteration 3 (length = 3):
  remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0
  remainder is 0! We found a solution.
  Return length = 3.
  The smallest repunit divisible by 3 is 111.


Let's walk through with k = 7:

Initial state: k = 7. k is not divisible by 2 or 5. remainder = 0.

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
  remainder is 0! We found a solution.
  Return length = 6.
  The smallest repunit divisible by 7 is 111111.


---

## 📊 Complexity Analysis

### Time Complexity
O(k) - The loop iterates at most k times. In each iteration, we perform constant time arithmetic operations (multiplication, addition, modulo). Therefore, the time complexity is directly proportional to k.

### Space Complexity
O(1) - We only use a few variables (`k`, `remainder`, `length`) to store intermediate values. The amount of memory used does not grow with the input size k, making it constant space.

---

## ⚠️ Edge Cases

- k = 1: The smallest repunit is 1, length is 1.
- k is even (e.g., k = 2, 4, 6): No solution exists, should return -1.
- k is a multiple of 5 (e.g., k = 5, 10, 15): No solution exists, should return -1.
- k is a prime number not 2 or 5 (e.g., k = 3, 7, 11): A solution will always exist and be found within k iterations.

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
*Generated on 2025-11-27 15:27:51*
