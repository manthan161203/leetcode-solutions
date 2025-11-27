# Smallest Integer Divisible by K

**Difficulty:** 🟡 Medium

**Tags:** math, number theory, simulation

---

## 📝 Problem Statement
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1. Return the length of n. If there is no such n, return -1. Note: n may not fit in a 64-bit signed integer.

---

## 💡 Explanation
The problem asks for the length of the smallest positive integer composed solely of the digit '1' that is divisible by a given positive integer 'k'. If no such integer exists, we should return -1. The key insight is that we can simulate the construction of these '1'-only numbers and check for divisibility by 'k' without actually forming the large numbers, which could exceed standard integer limits. We can do this by keeping track of the remainder when the current '1'-only number is divided by 'k'.

---

## 🎯 Hints
- Consider the properties of divisibility by 2 and 5. If k is divisible by 2 or 5, can a number consisting only of 1s ever be divisible by k?
- Think about how to generate numbers like 1, 11, 111, 1111, etc., efficiently. How does the next number relate to the previous one?
- Instead of forming the full number, can you work with remainders modulo k?
- What is the maximum possible length of the repeating sequence of remainders? If you encounter a remainder you've seen before, what does that imply?
- The problem states that 'n' may not fit in a 64-bit signed integer. This strongly suggests an approach that avoids explicitly constructing 'n'.

---

## 🔍 Algorithm
**Iterative Remainder Calculation**

### Approach Steps
- Handle immediate impossible cases: If k is divisible by 2 or 5, no number consisting only of 1s can be divisible by k. Return -1.
- Initialize a variable `remainder` to 0. This will store the remainder of the current '1'-only number when divided by k.
- Iterate through possible lengths of the '1'-only number, starting from 1. The maximum possible length we need to check is k, because if a repeating pattern of remainders occurs before length k, we would have already found a solution or detected an infinite loop.
- In each iteration (representing an increase in length by 1):
-   Update the `remainder`: The new number is formed by appending a '1' to the previous number. Mathematically, if the previous number was `N`, the new number is `N * 10 + 1`. So, the new remainder is `(previous_remainder * 10 + 1) % k`.
-   Check for divisibility: If the `remainder` becomes 0, it means the current '1'-only number is divisible by k. Return the current `length`.
- If the loop completes without finding a remainder of 0 (i.e., after checking up to length k), it implies no such number exists. Return -1.

---

## 📊 Complexity
- **Time Complexity:** O(k). The loop runs at most k times because if a remainder repeats, we are in a cycle. Since there are only k possible remainders (0 to k-1), a remainder must repeat within k+1 steps. The first k steps are guaranteed to produce distinct remainders if no solution is found before then.
- **Space Complexity:** O(1). We only use a few variables (`remainder`, `length`) to store state, regardless of the input size k.

---

## 🚶 Walkthrough
Let's trace with k = 3:

1. **Check divisibility by 2 or 5:** k=3 is not divisible by 2 or 5. Proceed.
2. **Initialization:** `remainder = 0`, `length = 1`.
3. **Iteration 1 (length = 1):**
   - `remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1`.
   - `remainder` is not 0.
4. **Iteration 2 (length = 2):**
   - `remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2`.
   - `remainder` is not 0.
5. **Iteration 3 (length = 3):**
   - `remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0`.
   - `remainder` is 0! We found a solution.
   - Return `length`, which is 3. The number is 111, and 111 / 3 = 37.

Let's trace with k = 2:

1. **Check divisibility by 2 or 5:** k=2 is divisible by 2. Return -1 immediately.

Let's trace with k = 7:

1. **Check divisibility by 2 or 5:** k=7 is not divisible by 2 or 5. Proceed.
2. **Initialization:** `remainder = 0`, `length = 1`.
3. **Iteration 1 (length = 1):** `remainder = (0 * 10 + 1) % 7 = 1`.
4. **Iteration 2 (length = 2):** `remainder = (1 * 10 + 1) % 7 = 11 % 7 = 4`.
5. **Iteration 3 (length = 3):** `remainder = (4 * 10 + 1) % 7 = 41 % 7 = 6`.
6. **Iteration 4 (length = 4):** `remainder = (6 * 10 + 1) % 7 = 61 % 7 = 5`.
7. **Iteration 5 (length = 5):** `remainder = (5 * 10 + 1) % 7 = 51 % 7 = 2`.
8. **Iteration 6 (length = 6):** `remainder = (2 * 10 + 1) % 7 = 21 % 7 = 0`.
   - `remainder` is 0! We found a solution.
   - Return `length`, which is 6. The number is 111111, and 111111 / 7 = 15873.

---

## ⚠️ Edge Cases
- k = 1: The smallest '1'-only number is 1, which is divisible by 1. Length is 1. The code handles this: `remainder = (0 * 10 + 1) % 1 = 0`. Returns 1.
- k is divisible by 2 (e.g., k=2, k=4, k=6): No '1'-only number can end in an even digit, so it cannot be divisible by 2. The code correctly returns -1.
- k is divisible by 5 (e.g., k=5, k=10, k=15): No '1'-only number can end in 0 or 5, so it cannot be divisible by 5. The code correctly returns -1.
- k is a prime number not 2 or 5 (e.g., k=3, k=7, k=11): The algorithm will find a solution. For k=3, length is 3. For k=7, length is 6. For k=11, length is 2 (11).
- k is a composite number not divisible by 2 or 5 (e.g., k=9, k=21): The algorithm will find a solution. For k=9, length is 9 (111111111). For k=21, length is 6 (111111).

Generated on 2025-11-27 15:20:05.593674
