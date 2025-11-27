# 1015. Smallest Integer Divisible by K

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Math`, `Number Theory`, `Simulation`

---

## 📝 Problem Statement

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.  Return the length of n. If there is no such n, return -1.  Note: n may not fit in a 64-bit signed integer.     Example 1:  Input: k = 1 Output: 1 Explanation: The smallest answer is n = 1, which has length 1. Example 2:  Input: k = 2 Output: -1 Explanation: There is no such positive integer n divisible by 2. Example 3:  Input: k = 3 Output: 3 Explanation: The smallest answer is n = 111, which has length 3.    Constraints:  1 <= k <= 105

### Input
A positive integer k.

### Output
The length of the smallest positive integer n divisible by k and consisting only of the digit 1. Return -1 if no such integer exists.

---

## 💡 Explanation

The solution iteratively constructs numbers consisting only of '1's and checks their divisibility by k. It leverages the property that the remainder of a number formed by appending '1' to a previous number is (previous_remainder * 10 + 1) % k. This avoids large number arithmetic and efficiently finds the smallest length.

---

## 🎯 Hints

1. Consider the structure of the numbers: 1, 11, 111, 1111, etc. These can be represented as (10^length - 1) / 9.
2. Instead of calculating these large numbers, focus on their remainders when divided by k. This is a key insight for avoiding overflow.
3. The remainder of a number formed by appending '1' to a previous number can be calculated using the previous remainder: `new_remainder = (previous_remainder * 10 + 1) % k`.
4. If k is divisible by 2 or 5, no number consisting only of '1's can be divisible by k. This is because such numbers are always odd and do not end in 0 or 5.
5. The problem guarantees that if a solution exists, it will be found within k iterations. This is due to the Pigeonhole Principle: there are only k possible remainders (0 to k-1). If we don't find a remainder of 0 within k steps, we must have encountered a repeating remainder, indicating no solution.
6. The maximum length of the smallest repunit divisible by k can be at most k.

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

1. Handle the immediate edge case: if k is even or divisible by 5, return -1, as no repunit can be divisible by them.
2. Initialize a variable `remainder` to 0. This will store the remainder of the current repunit number when divided by k.
3. Iterate through possible lengths of the repunit number, starting from 1 up to k. The maximum possible length is k due to the Pigeonhole Principle.
4. In each iteration, update the `remainder` using the formula: `remainder = (remainder * 10 + 1) % k`. This simulates appending a '1' to the current repunit and calculating the new remainder.
5. If the `remainder` becomes 0 at any point, it means the current repunit number is divisible by k. Return the current `length` as it's the smallest such number.
6. If the loop completes without finding a remainder of 0, it means no such repunit exists within the possible lengths, so return -1.

---

## 🚶 Step-by-Step Walkthrough

```
Input: k = 3
Initialize: remainder = 0

--- length = 1 ---
remainder = (0 * 10 + 1) % 3 = 1 % 3 = 1
remainder is not 0.
  remainder: 1

--- length = 2 ---
remainder = (1 * 10 + 1) % 3 = 11 % 3 = 2
remainder is not 0.
  remainder: 2

--- length = 3 ---
remainder = (2 * 10 + 1) % 3 = 21 % 3 = 0
remainder is 0. Return length.

Final Answer: 3
```

```
Input: k = 7
Initialize: remainder = 0

--- length = 1 ---
remainder = (0 * 10 + 1) % 7 = 1 % 7 = 1
remainder is not 0.
  remainder: 1

--- length = 2 ---
remainder = (1 * 10 + 1) % 7 = 11 % 7 = 4
remainder is not 0.
  remainder: 4

--- length = 3 ---
remainder = (4 * 10 + 1) % 7 = 41 % 7 = 6
remainder is not 0.
  remainder: 6

--- length = 4 ---
remainder = (6 * 10 + 1) % 7 = 61 % 7 = 5
remainder is not 0.
  remainder: 5

--- length = 5 ---
remainder = (5 * 10 + 1) % 7 = 51 % 7 = 2
remainder is not 0.
  remainder: 2

--- length = 6 ---
remainder = (2 * 10 + 1) % 7 = 21 % 7 = 0
remainder is 0. Return length.

Final Answer: 6
```

```
Input: k = 2
Check initial condition: k % 2 == 0 is true.
Return -1.

Final Answer: -1
```

---

## 📊 Complexity Analysis

### Time Complexity
O(k) - The loop iterates at most k times. In each iteration, we perform constant time arithmetic operations (multiplication, addition, modulo). Therefore, the time complexity is directly proportional to k.

### Space Complexity
O(1) - The solution uses only a few variables (`remainder`, `length`) to store intermediate values. The amount of memory used does not grow with the input size k, making it constant space.

---

## ⚠️ Edge Cases

- k = 1: The smallest repunit is 1, which is divisible by 1. Length is 1.
- k is even (e.g., k = 2, 4, 6): No repunit can be divisible by an even number, so the result should be -1.
- k is divisible by 5 (e.g., k = 5, 10, 15): No repunit can be divisible by 5, so the result should be -1.
- k has prime factors other than 2 and 5 (e.g., k = 3, 7, 11): These cases will have a solution and are handled by the iterative remainder calculation.

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
*Generated on 2025-11-27 15:12:44*
