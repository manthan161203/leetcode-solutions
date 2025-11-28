# 1018. Binary Prefix Divisible By 5

**Difficulty:** 🟢 EASY

**Topics/Tags:** `Array`, `Math`, `Bit Manipulation`

---

## 📝 Problem Statement

You are given a binary array `nums` (0-indexed).

We define `xi` as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

For example, if `nums = [1,0,1]`, then `x0 = 1`, `x1 = 2`, and `x2 = 5`.

Return an array of booleans `answer` where `answer[i]` is true if `xi` is divisible by 5.

### Example 1:

**Input:** `nums = [0,1,1]`
**Output:** `[true,false,false]`
**Explanation:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10. Only the first number is divisible by 5, so `answer[0]` is true.

### Example 2:

**Input:** `nums = [1,1,1]`
**Output:** `[false,false,false]`

### Constraints:

*   `1 <= nums.length <= 10^5`
*   `nums[i]` is either `0` or `1`.

### Input
A binary array `nums` where each element is either 0 or 1.

### Output
An array of booleans where `answer[i]` is true if the binary number formed by `nums[0..i]` is divisible by 5, and false otherwise.

---


## 💡 Explanation

The solution iterates through the binary array `nums`, progressively building the integer represented by the prefix. Instead of converting the entire binary string to an integer at each step (which can lead to overflow for large inputs), it leverages **modular arithmetic**. Specifically, it keeps track of the number modulo 5. When a new bit is appended, the current number is effectively multiplied by 2 and the new bit is added. This operation is performed modulo 5 to maintain a manageable number. The result for each prefix is determined by checking if this running modulo 5 value is 0.

---

## 🔑 Key Insights

1. The core idea is to use **modular arithmetic** to avoid large number computations. We only care about the remainder when divided by 5.
2. When appending a new bit `b` to a binary number `x`, the new number becomes `x * 2 + b`. This transformation can be applied directly to the remainders modulo 5: `(x * 2 + b) % 5`.
3. The problem can be solved by maintaining a **running remainder** modulo 5 as we traverse the array.
4. The divisibility by 5 depends only on the last digit of a number in base 10. In binary, divisibility by 5 is more complex but can be efficiently tracked using the running remainder.

---

## 🎯 Hints

1. Consider how to calculate the next prefix number from the current one. If the current prefix represents number `N`, adding a bit `b` (0 or 1) at the end makes the new number `N * 2 + b`.
2. Instead of calculating the full integer `N`, focus on its **remainder modulo 5**.
3. Apply the modular arithmetic property: `(a + b) % m = ((a % m) + (b % m)) % m` and `(a * b) % m = ((a % m) * (b % m)) % m`.
4. Maintain a variable that stores the **current prefix number modulo 5**.
5. For each bit, update this running remainder using the formula: `new_remainder = (current_remainder * 2 + current_bit) % 5`.
6. The answer for a prefix is `true` if its corresponding running remainder modulo 5 is 0.

---

## 🔍 Algorithm

```
function prefixesDivBy5(nums):
  result = an empty list of booleans
  current_remainder = 0

  for each bit in nums:
    # Update the current remainder using modular arithmetic
    # The new number is (previous_number * 2 + current_bit)
    # So, the new remainder is (previous_remainder * 2 + current_bit) % 5
    current_remainder = (current_remainder * 2 + bit) % 5

    # Check if the current prefix number is divisible by 5
    if current_remainder == 0:
      append true to result
    else:
      append false to result

  return result
```

---

## 📋 Approach

1. Initialize an empty list `result` to store the boolean answers.
2. Initialize a variable `current_remainder` to 0. This will store the remainder of the current prefix number when divided by 5.
3. Iterate through each `bit` in the input array `nums`.
4. For each `bit`, update `current_remainder` using the formula: `current_remainder = (current_remainder * 2 + bit) % 5`.
5. After updating `current_remainder`, check if it is equal to 0.
6. If `current_remainder` is 0, append `true` to the `result` list, indicating that the current prefix number is divisible by 5.
7. Otherwise (if `current_remainder` is not 0), append `false` to the `result` list.
8. After iterating through all bits, return the `result` list.

---

## 🚶 Step-by-Step Walkthrough

Let's walk through `nums = [0, 1, 1]`:

Initial state:
`result = []`
`current_remainder = 0`

--- Step 1: Process `nums[0] = 0` ---

*   **Action:** Update `current_remainder`.
    `current_remainder = (0 * 2 + 0) % 5 = 0 % 5 = 0`

*   **Check divisibility:** `current_remainder` is 0.

*   **Update result:** Append `true`.

State after Step 1:
`result = [true]`
`current_remainder = 0`

--- Step 2: Process `nums[1] = 1` ---

*   **Action:** Update `current_remainder`.
    `current_remainder = (0 * 2 + 1) % 5 = 1 % 5 = 1`

*   **Check divisibility:** `current_remainder` is 1 (not 0).

*   **Update result:** Append `false`.

State after Step 2:
`result = [true, false]`
`current_remainder = 1`

--- Step 3: Process `nums[2] = 1` ---

*   **Action:** Update `current_remainder`.
    `current_remainder = (1 * 2 + 1) % 5 = 3 % 5 = 3`

*   **Check divisibility:** `current_remainder` is 3 (not 0).

*   **Update result:** Append `false`.

State after Step 3:
`result = [true, false, false]`
`current_remainder = 3`

--- End of iteration ---

Final Result: `[true, false, false]`

Visualizing the numbers and their remainders:

| Index | Bit | Prefix Binary | Prefix Decimal | `current_remainder` (Before) | Calculation `(rem * 2 + bit) % 5` | `current_remainder` (After) | Divisible by 5? |
|-------|-----|---------------|----------------|------------------------------|-----------------------------------|-----------------------------|-----------------|
| 0     | 0   | 0             | 0              | 0                            | `(0 * 2 + 0) % 5 = 0`             | 0                           | ✓ (true)        |
| 1     | 1   | 01            | 1              | 0                            | `(0 * 2 + 1) % 5 = 1`             | 1                           | ✗ (false)       |
| 2     | 1   | 011           | 3              | 1                            | `(1 * 2 + 1) % 5 = 3`             | 3                           | ✗ (false)       |

---

## 📊 Complexity Analysis

### Time Complexity
**O(n)** - The algorithm iterates through the input array `nums` exactly once. For each element, it performs a constant number of arithmetic operations (multiplication, addition, modulo). Therefore, the time complexity is directly proportional to the number of elements in `nums`, denoted by `n`.

### Space Complexity
**O(1)** - The algorithm uses a constant amount of extra space. It only requires a few variables (`result`, `current_remainder`) to store intermediate values. The `result` list stores `n` booleans, but this is considered part of the output, not auxiliary space. If the output space is excluded, the space complexity is O(1). If the output space is included, it would be O(n). Typically, for complexity analysis, auxiliary space is considered, making it O(1).

---

## ⚠️ Edge Cases

- Array of size 1: `nums = [0]` should return `[true]`. `nums = [1]` should return `[false]`.
- Array with all zeros: `nums = [0, 0, 0]` should return `[true, true, true]`.
- Array with all ones: `nums = [1, 1, 1]` should return `[false, false, false]`.
- A very long array: The modular arithmetic approach is crucial here, as converting the full binary string to an integer would overflow standard integer types. The constraints `1 <= nums.length <= 10^5` highlight this.

---

## 📥 Examples

### Example 1
**Input:** `[0,1,1]`
**Output:** `[true,false,false]`

### Example 2
**Input:** `[1,1,1]`
**Output:** `[false,false,false]`

---
*Generated on 2025-11-28 12:08:21*
