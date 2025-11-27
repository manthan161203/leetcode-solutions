# 739. Daily Temperatures

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Array`, `Stack`

---

## 📝 Problem Statement

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

### Input
An array of integers `temperatures` representing the daily temperatures.

### Output
An array `answer` where `answer[i]` is the number of days to wait after the `i`th day for a warmer temperature. If no warmer temperature exists in the future, `answer[i]` is 0.

---

## 💡 Explanation

This solution uses a monotonic decreasing stack to efficiently find the next warmer day for each temperature. When a warmer temperature is encountered, it means we've found the next warmer day for all the previous cooler temperatures stored in the stack. The stack stores indices, allowing us to calculate the difference in days.

---

## 🎯 Hints

1. Think about how to efficiently find the *next* greater element for each item in an array.
2. A **stack** is a suitable data structure for problems involving finding the next greater element.
3. Maintain a **monotonic decreasing stack** to store indices of temperatures in decreasing order.
4. When you encounter a temperature greater than the top of the stack, it signifies a warmer day.
5. The difference between the current index and the popped index from the stack gives the number of days to wait.
6. If the stack is empty or no warmer day is found, the wait time is **0**.

---

## 🔍 Algorithm

```
function dailyTemperatures(temperatures):
  n = length of temperatures
  answer = array of size n, initialized with 0s
  stack = empty stack

  for i from 0 to n-1:
    current_temp = temperatures[i]
    while stack is not empty AND current_temp > temperatures[stack.top()]:
      previous_index = stack.pop()
      answer[previous_index] = i - previous_index
    stack.push(i)

  return answer
```

---

## 📋 Approach

1. Initialize an `answer` array of the same length as `temperatures` with all zeros.
2. Initialize an empty `stack` to store indices of temperatures.
3. Iterate through the `temperatures` array from left to right using index `i`.
4. For each `temperature[i]`, check if the `stack` is not empty and if `temperature[i]` is greater than the temperature at the index at the top of the `stack` (`temperatures[stack[-1]]`).
5. If the condition in the previous step is true, it means we've found a warmer day for the temperature at `stack[-1]`. Pop the index from the `stack` and update `answer[popped_index]` with the difference between the current index `i` and the `popped_index` (`i - popped_index`).
6. Repeat the popping process as long as the condition holds.
7. After the `while` loop (or if the condition was initially false), push the current index `i` onto the `stack`.
8. After iterating through all temperatures, return the `answer` array.

---

## 🚶 Step-by-Step Walkthrough

Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Initialize: answer = [0, 0, 0, 0, 0, 0, 0, 0], stack = []

--- i = 0, temp = 73 ---
  Stack is empty. Push 0.
  stack: [0]
  answer: [0, 0, 0, 0, 0, 0, 0, 0]

--- i = 1, temp = 74 ---
  Stack not empty. temperatures[1] (74) > temperatures[stack[-1]] (temperatures[0] = 73).
  Pop 0. answer[0] = 1 - 0 = 1
  stack: []
  answer: [1, 0, 0, 0, 0, 0, 0, 0]
  Push 1.
  stack: [1]
  answer: [1, 0, 0, 0, 0, 0, 0, 0]

--- i = 2, temp = 75 ---
  Stack not empty. temperatures[2] (75) > temperatures[stack[-1]] (temperatures[1] = 74).
  Pop 1. answer[1] = 2 - 1 = 1
  stack: []
  answer: [1, 1, 0, 0, 0, 0, 0, 0]
  Push 2.
  stack: [2]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 3, temp = 71 ---
  Stack not empty. temperatures[3] (71) <= temperatures[stack[-1]] (temperatures[2] = 75).
  Push 3.
  stack: [2, 3]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 4, temp = 69 ---
  Stack not empty. temperatures[4] (69) <= temperatures[stack[-1]] (temperatures[3] = 71).
  Push 4.
  stack: [2, 3, 4]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 5, temp = 72 ---
  Stack not empty. temperatures[5] (72) > temperatures[stack[-1]] (temperatures[4] = 69).
  Pop 4. answer[4] = 5 - 4 = 1
  stack: [2, 3]
  answer: [1, 1, 0, 0, 1, 0, 0, 0]
  Stack not empty. temperatures[5] (72) > temperatures[stack[-1]] (temperatures[3] = 71).
  Pop 3. answer[3] = 5 - 3 = 2
  stack: [2]
  answer: [1, 1, 0, 2, 1, 0, 0, 0]
  Stack not empty. temperatures[5] (72) <= temperatures[stack[-1]] (temperatures[2] = 75).
  Push 5.
  stack: [2, 5]
  answer: [1, 1, 0, 2, 1, 0, 0, 0]

--- i = 6, temp = 76 ---
  Stack not empty. temperatures[6] (76) > temperatures[stack[-1]] (temperatures[5] = 72).
  Pop 5. answer[5] = 6 - 5 = 1
  stack: [2]
  answer: [1, 1, 0, 2, 1, 1, 0, 0]
  Stack not empty. temperatures[6] (76) > temperatures[stack[-1]] (temperatures[2] = 75).
  Pop 2. answer[2] = 6 - 2 = 4
  stack: []
  answer: [1, 1, 4, 2, 1, 1, 0, 0]
  Push 6.
  stack: [6]
  answer: [1, 1, 4, 2, 1, 1, 0, 0]

--- i = 7, temp = 73 ---
  Stack not empty. temperatures[7] (73) <= temperatures[stack[-1]] (temperatures[6] = 76).
  Push 7.
  stack: [6, 7]
  answer: [1, 1, 4, 2, 1, 1, 0, 0]

End of loop.
Final Answer: [1, 1, 4, 2, 1, 1, 0, 0]

---

## 📊 Complexity Analysis

### Time Complexity
O(n) - Each element is pushed onto and popped from the stack at most once. The inner `while` loop processes elements that are popped, and since each element is popped at most once, the total work done by the `while` loop across all iterations is proportional to `n`.

### Space Complexity
O(n) - In the worst-case scenario (e.g., temperatures are in strictly decreasing order), the stack can store all `n` indices. Therefore, the space complexity is proportional to the number of elements in the input array.

---

## ⚠️ Edge Cases

- Array with only one element: `[30]` -> `[0]`
- Temperatures are in strictly increasing order: `[30, 40, 50, 60]` -> `[1, 1, 1, 0]`
- Temperatures are in strictly decreasing order: `[60, 50, 40, 30]` -> `[0, 0, 0, 0]`
- All temperatures are the same: `[70, 70, 70]` -> `[0, 0, 0]`
- A mix of increasing and decreasing sequences.

---

## 📥 Examples

### Example 1
**Input:** `temperatures = [73,74,75,71,69,72,76,73]`
**Output:** `[1,1,4,2,1,1,0,0]`

### Example 2
**Input:** `temperatures = [30,40,50,60]`
**Output:** `[1,1,1,0]`

### Example 3
**Input:** `temperatures = [30,60,90]`
**Output:** `[1,1,0]`

---
*Generated on 2025-11-27 15:09:29*
