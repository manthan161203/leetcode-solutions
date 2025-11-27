# 1015. Smallest Integer Divisible by K

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Math`, `Number Theory`, `Simulation`

---

## 📝 Problem Statement

Given a positive integer `k`, you need to find the length of the smallest positive integer `n` such that `n` is divisible by `k`, and `n` only contains the digit `1`.

Return the length of `n`. If there is no such `n`, return `-1`.

**Note:** `n` may not fit in a 64-bit signed integer.

### Example 1:

**Input:** `k = 1`
**Output:** `1`
**Explanation:** The smallest answer is `n = 1`, which has length 1.

### Example 2:

**Input:** `k = 2`
**Output:** `-1`
**Explanation:** There is no such positive integer `n` divisible by 2.

### Example 3:

**Input:** `k = 3`
**Output:** `3`
**Explanation:** The smallest answer is `n = 111`, which has length 3.

### Constraints:

*   `1 <= k <= 10^5`

### Input
A positive integer `k`.

### Output
The length of the smallest positive integer `n` composed solely of the digit '1' that is divisible by `k`. Returns -1 if no such integer exists.

---

## 💡 Explanation

The solution leverages the property of modular arithmetic to efficiently find the smallest repunit (a number consisting only of ones) divisible by `k`. It iteratively constructs repunits by appending '1' and taking the remainder modulo `k`. If the remainder becomes 0, the current length is the answer. The core insight is that we only need to track the **remainder** because the divisibility by `k` depends solely on the remainder. If `k` is divisible by 2 or 5, no such repunit exists, as repunits are always odd and do not end in 0 or 5.

---

## 🎯 Hints

1. Consider the properties of numbers formed by only the digit '1'. These are called **repunits**.
2. Think about how to check for divisibility by `k` without constructing the entire large number. **Modular arithmetic** is key here.
3. When you append a '1' to a number `N`, the new number is `N * 10 + 1`. How does this relate to remainders?
4. If `k` is divisible by 2 or 5, can a number consisting only of '1's ever be divisible by `k`? Think about the last digit.
5. The problem states that `n` may not fit in a 64-bit integer. This strongly suggests an approach that avoids explicit large number construction, focusing on **remainders**.
6. What happens if we encounter a **repeated remainder** during our iterative process? This indicates a cycle and that no solution will be found.

---

## 🔍 Algorithm

```
function smallestRepunitDivByK(k):
  // Check for immediate impossibility
  if k is divisible by 2 or k is divisible by 5:
    return -1

  // Initialize remainder and length
  remainder = 0
  length = 0

  // Iterate up to k times (Pigeonhole Principle guarantees a cycle within k steps)
  for length from 1 to k:
    // Construct the next repunit's remainder: (previous_remainder * 10 + 1) % k
    remainder = (remainder * 10 + 1) % k

    // If the remainder is 0, we found a divisible repunit
    if remainder == 0:
      return length

  // If loop finishes without finding a solution, it's impossible
  return -1
```

---

## 📋 Approach

1. **Handle impossible cases**: If `k` is even or divisible by 5, return -1 immediately, as repunits (numbers of only 1s) cannot be divisible by them.
2. **Initialize variables**: Set `remainder` to 0 and `length` to 0.
3. **Iterate and calculate remainders**: Loop from `length = 1` up to `k`. In each iteration, update the `remainder` using the formula `(remainder * 10 + 1) % k`. This simulates appending a '1' to the current repunit and finding its remainder when divided by `k`.
4. **Check for divisibility**: Inside the loop, if the `remainder` becomes 0, it means the repunit of the current `length` is divisible by `k`. Return `length`.
5. **Handle no solution**: If the loop completes without the `remainder` ever becoming 0, it implies no such repunit exists. Return -1.

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

Smallest repunit is 111, which is 3 * 37. Length is 3.


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

Smallest repunit is 111111, which is 7 * 15873. Length is 6.

---

## 📊 Complexity Analysis

### Time Complexity
**O(k)** - The loop iterates at most `k` times. In each iteration, we perform constant time arithmetic operations (multiplication, addition, modulo). According to the Pigeonhole Principle, if we haven't found a remainder of 0 within `k` steps, we must have encountered a repeated remainder, indicating a cycle, and thus no solution will be found. Therefore, the maximum number of iterations is bounded by `k`.

### Space Complexity
**O(1)** - The solution uses only a few variables (`k`, `remainder`, `length`) to store intermediate values. The amount of memory used does not grow with the input size `k`. Therefore, the space complexity is constant.

---

## ⚠️ Edge Cases

- k = 1: The smallest repunit is 1, length is 1. The code handles this correctly as (0*10+1)%1 = 0, returning 1.
- k is even (e.g., k = 2, k = 4, k = 6): The code correctly returns -1 due to the initial check `k % 2 == 0`.
- k is divisible by 5 (e.g., k = 5, k = 10, k = 15): The code correctly returns -1 due to the initial check `k % 5 == 0`.
- k is a prime number (e.g., k = 3, k = 7, k = 11): The algorithm will find a solution if one exists, as demonstrated in the walkthroughs.

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
*Generated on 2025-11-27 17:26:11*
