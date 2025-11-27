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

This solution uses a monotonic decreasing stack to efficiently find the next warmer day for each temperature. The stack stores indices of days for which we haven't found a warmer day yet. When we encounter a new day with a warmer temperature, we pop elements from the stack, calculate the difference in days, and update the answer for those popped days.

---

## 🎯 Hints

1. Think about how to efficiently find the *next greater element* for each element in an array.
2. A **stack** is a suitable data structure for problems involving finding the next greater/smaller element.
3. Maintain a **monotonic stack** (e.g., decreasing order of temperatures) to keep track of potential candidates for future warmer days.
4. When a warmer day is found, it resolves the waiting period for all previous colder days on the stack that are now 'obsolete'.
5. Store **indices** in the stack, not the temperatures themselves, to easily calculate the difference in days.
6. Initialize the `answer` array with zeros, as this is the default value if no warmer day is found.

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
      previous_day_index = stack.pop()
      answer[previous_day_index] = i - previous_day_index
    stack.push(i)

  return answer
```

---

## 📋 Approach

1. Initialize an `answer` array of the same size as `temperatures`, filled with zeros.
2. Initialize an empty `stack` to store indices of days.
3. Iterate through the `temperatures` array from left to right using an index `i`.
4. For each `temperatures[i]`, check if the stack is not empty and if `temperatures[i]` is greater than the temperature at the index at the top of the stack (`temperatures[stack.top()]`).
5. If it is warmer, pop the index from the stack. This popped index represents a day for which `temperatures[i]` is the next warmer day. Calculate the difference `i - popped_index` and store it in `answer[popped_index]`.
6. Repeat the popping process as long as the condition in step 4 holds.
7. After the `while` loop (or if the condition was initially false), push the current index `i` onto the stack.
8. After iterating through all temperatures, return the `answer` array.

---

## 🚶 Step-by-Step Walkthrough

```
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Initialize: answer = [0, 0, 0, 0, 0, 0, 0, 0], stack = []

--- i = 0, temp = 73 ---
Stack is empty. Push 0.
  stack: [0]
  answer: [0, 0, 0, 0, 0, 0, 0, 0]

--- i = 1, temp = 74 ---
Stack not empty. temperatures[1] (74) > temperatures[stack.top()=0] (73).
Pop 0. answer[0] = 1 - 0 = 1
  stack: []
  answer: [1, 0, 0, 0, 0, 0, 0, 0]
Push 1.
  stack: [1]
  answer: [1, 0, 0, 0, 0, 0, 0, 0]

--- i = 2, temp = 75 ---
Stack not empty. temperatures[2] (75) > temperatures[stack.top()=1] (74).
Pop 1. answer[1] = 2 - 1 = 1
  stack: []
  answer: [1, 1, 0, 0, 0, 0, 0, 0]
Push 2.
  stack: [2]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 3, temp = 71 ---
Stack not empty. temperatures[3] (71) <= temperatures[stack.top()=2] (75).
Push 3.
  stack: [2, 3]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 4, temp = 69 ---
Stack not empty. temperatures[4] (69) <= temperatures[stack.top()=3] (71).
Push 4.
  stack: [2, 3, 4]
  answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 5, temp = 72 ---
Stack not empty. temperatures[5] (72) > temperatures[stack.top()=4] (69).
Pop 4. answer[4] = 5 - 4 = 1
  stack: [2, 3]
  answer: [1, 1, 0, 0, 1, 0, 0, 0]
Stack not empty. temperatures[5] (72) > temperatures[stack.top()=3] (71).
Pop 3. answer[3] = 5 - 3 = 2
  stack: [2]
  answer: [1, 1, 0, 2, 1, 0, 0, 0]
Stack not empty. temperatures[5] (72) <= temperatures[stack.top()=2] (75).
Push 5.
  stack: [2, 5]
  answer: [1, 1, 0, 2, 1, 0, 0, 0]

--- i = 6, temp = 76 ---
Stack not empty. temperatures[6] (76) > temperatures[stack.top()=5] (72).
Pop 5. answer[5] = 6 - 5 = 1
  stack: [2]
  answer: [1, 1, 0, 2, 1, 1, 0, 0]
Stack not empty. temperatures[6] (76) > temperatures[stack.top()=2] (75).
Pop 2. answer[2] = 6 - 2 = 4
  stack: []
  answer: [1, 1, 4, 2, 1, 1, 0, 0]
Push 6.
  stack: [6]
  answer: [1, 1, 4, 2, 1, 1, 0, 0]

--- i = 7, temp = 73 ---
Stack not empty. temperatures[7] (73) <= temperatures[stack.top()=6] (76).
Push 7.
  stack: [6, 7]
  answer: [1, 1, 4, 2, 1, 1, 0, 0]

End of loop.
Final Answer: [1, 1, 4, 2, 1, 1, 0, 0]
```

---

## 📊 Complexity Analysis

### Time Complexity
O(n) - Each element is pushed onto the stack and popped from the stack at most once. The outer loop iterates through the array once, and the inner `while` loop's total operations across all outer loop iterations are bounded by `n` pops.

### Space Complexity
O(n) - In the worst case, the stack can store all indices if the temperatures are in strictly decreasing order (e.g., [100, 99, 98, ...]).

---

## ⚠️ Edge Cases

- Array with only one element: The loop will run once, the stack will be empty, the element will be pushed, and the function will return `[0]`.
- Temperatures are strictly increasing: Each element will be warmer than the previous, leading to `n-1` pops and `n-1` calculations, with the last element remaining on the stack.
- Temperatures are strictly decreasing: No element will be warmer than the previous, so all indices will be pushed onto the stack, and the `answer` array will remain all zeros.
- All temperatures are the same: Similar to strictly decreasing, no warmer day will be found, and the `answer` array will be all zeros.

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
*Generated on 2025-11-27 15:11:31*
