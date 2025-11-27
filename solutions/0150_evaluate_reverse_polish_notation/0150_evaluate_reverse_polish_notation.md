# 150. Evaluate Reverse Polish Notation

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Array`, `Stack`

---

## 📝 Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

**Note that:**

*   The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
*   Each operand may be an integer or another expression.
*   The division between two integers always truncates toward zero.
*   There will not be any division by zero.
*   The input represents a valid arithmetic expression in a reverse polish notation.
*   The answer and all the intermediate calculations can be represented in a 32-bit integer.

### Example 1:

**Input:** `tokens = ["2","1","+","3","*"]`
**Output:** `9`
**Explanation:** `((2 + 1) * 3) = 9`

### Example 2:

**Input:** `tokens = ["4","13","5","/","+"]`
**Output:** `6`
**Explanation:** `(4 + (13 / 5)) = 6`

### Example 3:

**Input:** `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`
**Output:** `22`
**Explanation:** `((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = ((10 * (6 / (12 * -11))) + 17) + 5 = ((10 * (6 / -132)) + 17) + 5 = ((10 * 0) + 17) + 5 = (0 + 17) + 5 = 17 + 5 = 22

### Constraints:

*   `1 <= tokens.length <= 10^4`
*   `tokens[i]` is either an operator: `'+'`, `'-'`, `'*'`, or `'/'`, or an integer in the range `[-200, 200]`.

### Input
An array of strings `tokens` representing an arithmetic expression in Reverse Polish Notation.

### Output
An integer representing the evaluated value of the arithmetic expression.

---

## 💡 Explanation

This solution evaluates a Reverse Polish Notation (RPN) expression using a **stack**. It iterates through the tokens: if a token is a number, it's pushed onto the stack. If it's an operator, the top two numbers are popped, the operation is performed, and the result is pushed back. The final result is the last element remaining on the stack.

---

## 🎯 Hints

1. A **stack** is the ideal data structure for evaluating RPN because of its Last-In, First-Out (LIFO) nature, perfectly mirroring how RPN operations are applied.
2. When you encounter an **operator**, you need the two most recently seen **operands** to perform the calculation.
3. Remember that in RPN, the order of operands matters for subtraction and division. The second-to-last element popped is the left operand, and the last element popped is the right operand.
4. Integers in RPN can be negative. Ensure your parsing handles this correctly.
5. The problem specifies that division should **truncate toward zero**. Be mindful of how your programming language handles integer division.
6. The final result of the expression will be the **single element** left on the stack after processing all tokens.

---

## 🔍 Algorithm

```
function evaluateRPN(tokens):
  stack = empty list
  operators = set of '+', '-', '*', '/'

  for each token in tokens:
    if token is not in operators:
      // It's an operand (number)
      push integer value of token onto stack
    else:
      // It's an operator
      operand2 = pop from stack  // Right operand
      operand1 = pop from stack  // Left operand

      result = 0
      if token is '+':
        result = operand1 + operand2
      else if token is '-':
        result = operand1 - operand2
      else if token is '*':
        result = operand1 * operand2
      else if token is '/':
        // Truncate toward zero
        result = floor(operand1 / operand2) if operand1 * operand2 >= 0 else ceil(operand1 / operand2)

      push result onto stack

  return the top element of the stack
```

---

## 📋 Approach

1. Initialize an empty **stack** to store operands.
2. Iterate through each `token` in the input `tokens` array.
3. If the `token` is an operator ('+', '-', '*', '/'):
4.   Pop the top two elements from the stack. The first popped is the right operand (`b`), and the second popped is the left operand (`a`).
5.   Perform the operation (`a` operator `b`).
6.   Handle integer division by truncating towards zero.
7.   Push the result of the operation back onto the stack.
8. If the `token` is not an operator, it's an operand (a number):
9.   Convert the `token` to an integer and push it onto the stack.
10. After iterating through all tokens, the final result will be the only element remaining on the stack. Return this element.

---

## 🚶 Step-by-Step Walkthrough

Let's walk through `tokens = ["2", "1", "+", "3", "*"]`:

1. **Token: "2"**
   - It's an operand.
   - Push `2` onto the stack.
   - Stack: `[2]`

2. **Token: "1"**
   - It's an operand.
   - Push `1` onto the stack.
   - Stack: `[2, 1]`

3. **Token: "+"**
   - It's an operator.
   - Pop `1` (b).
   - Pop `2` (a).
   - Calculate `a + b` -> `2 + 1 = 3`.
   - Push `3` onto the stack.
   - Stack: `[3]`

4. **Token: "3"**
   - It's an operand.
   - Push `3` onto the stack.
   - Stack: `[3, 3]`

5. **Token: "*"**
   - It's an operator.
   - Pop `3` (b).
   - Pop `3` (a).
   - Calculate `a * b` -> `3 * 3 = 9`.
   - Push `9` onto the stack.
   - Stack: `[9]`

End of tokens. The final result is the top of the stack: `9`.

---

## 📊 Complexity Analysis

### Time Complexity
**O(n)** - We iterate through the `tokens` array exactly once. Each token is processed in constant time (pushing/popping from the stack, arithmetic operations). Therefore, the time complexity is directly proportional to the number of tokens, `n`.

### Space Complexity
**O(n)** - In the worst-case scenario, if all tokens are operands (numbers), they will all be pushed onto the stack. This means the stack can grow to hold up to `n` elements, where `n` is the number of tokens. Therefore, the space complexity is proportional to `n`.

---

## ⚠️ Edge Cases

- Array with a single token (which must be an integer).
- Expressions involving only addition and subtraction.
- Expressions involving only multiplication and division.
- Expressions with negative operands and intermediate results.
- Expressions where division results in zero (e.g., `6 / 132` truncates to `0`).
- Expressions that result in large positive or negative numbers within the 32-bit integer range.

---

## 📥 Examples

### Example 1
**Input:** `["2","1","+","3","*"]`
**Output:** `9`

### Example 2
**Input:** `["4","13","5","/","+"]`
**Output:** `6`

### Example 3
**Input:** `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`
**Output:** `22`

---
*Generated on 2025-11-27 17:28:56*
