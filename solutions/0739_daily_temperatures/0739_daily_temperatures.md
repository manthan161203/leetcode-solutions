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

This solution uses a monotonic decreasing stack to efficiently find the next warmer day for each temperature. When a warmer temperature is encountered, it means we've found the answer for all previous days whose temperatures are less than the current one and are still on the stack. The stack stores indices of days for which we haven't yet found a warmer day.

---

## 🎯 Hints

1. Think about how to efficiently find the *next* greater element for each item in an array.
2. A **stack** is a suitable data structure for problems involving finding the next greater/smaller element.
3. Maintain a **monotonic decreasing stack** of indices. This means temperatures at indices in the stack will always be in decreasing order from bottom to top.
4. When you encounter a new temperature, compare it with the temperature at the index on top of the stack.
5. If the current temperature is warmer, it means you've found the next warmer day for the day(s) on the stack. Pop them and calculate the difference.
6. If the current temperature is not warmer, push its index onto the stack to maintain the decreasing order.

---

## 🔍 Algorithm

```
function dailyTemperatures(temperatures):
  n = length of temperatures
  answer = array of size n, initialized with 0s
  stack = empty list (will store indices)

  for i from 0 to n-1:
    current_temperature = temperatures[i]

    // While the stack is not empty AND the current temperature is warmer than the temperature at the index on top of the stack
    while stack is not empty AND current_temperature > temperatures[stack.top()]:
      // Pop the index of the day for which we've found the next warmer day
      previous_day_index = stack.pop()
      // Calculate the number of days to wait and store it in the answer array
      answer[previous_day_index] = i - previous_day_index

    // Push the current day's index onto the stack
    stack.push(i)

  return answer
```

---

## 📋 Approach

1. Initialize an empty stack to store indices of days.
2. Initialize an answer array of the same size as the temperatures array, filled with zeros.
3. Iterate through the temperatures array from left to right, using the index `i`.
4. For each `current_temperature` at index `i`, check the stack.
5. While the stack is not empty and the `current_temperature` is greater than the temperature at the index at the top of the stack:
6.   Pop the index from the stack. This index represents a day for which we've found the next warmer day.
7.   Calculate the difference between the current index `i` and the popped index. This is the number of days to wait.
8.   Store this difference in the `answer` array at the popped index.
9. After the while loop (or if the condition was never met), push the current index `i` onto the stack.
10. After iterating through all temperatures, return the `answer` array.

---

## 🚶 Step-by-Step Walkthrough

Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Initialize: answer = [0, 0, 0, 0, 0, 0, 0, 0], stack = []

--- i = 0, temp = 73 ---
stack is empty. Push 0.
stack: [0]
answer: [0, 0, 0, 0, 0, 0, 0, 0]

--- i = 1, temp = 74 ---
stack not empty. temperatures[1] (74) > temperatures[stack.top()=0] (73).
  Pop 0. answer[0] = 1 - 0 = 1.
stack: []
answer: [1, 0, 0, 0, 0, 0, 0, 0]
Push 1.
stack: [1]
answer: [1, 0, 0, 0, 0, 0, 0, 0]

--- i = 2, temp = 75 ---
stack not empty. temperatures[2] (75) > temperatures[stack.top()=1] (74).
  Pop 1. answer[1] = 2 - 1 = 1.
stack: []
answer: [1, 1, 0, 0, 0, 0, 0, 0]
Push 2.
stack: [2]
answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 3, temp = 71 ---
stack not empty. temperatures[3] (71) <= temperatures[stack.top()=2] (75).
Push 3.
stack: [2, 3]
answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 4, temp = 69 ---
stack not empty. temperatures[4] (69) <= temperatures[stack.top()=3] (71).
Push 4.
stack: [2, 3, 4]
answer: [1, 1, 0, 0, 0, 0, 0, 0]

--- i = 5, temp = 72 ---
stack not empty. temperatures[5] (72) > temperatures[stack.top()=4] (69).
  Pop 4. answer[4] = 5 - 4 = 1.
stack: [2, 3]
answer: [1, 1, 0, 0, 1, 0, 0, 0]
stack not empty. temperatures[5] (72) > temperatures[stack.top()=3] (71).
  Pop 3. answer[3] = 5 - 3 = 2.
stack: [2]
answer: [1, 1, 0, 2, 1, 0, 0, 0]
stack not empty. temperatures[5] (72) <= temperatures[stack.top()=2] (75).
Push 5.
stack: [2, 5]
answer: [1, 1, 0, 2, 1, 0, 0, 0]

--- i = 6, temp = 76 ---
stack not empty. temperatures[6] (76) > temperatures[stack.top()=5] (72).
  Pop 5. answer[5] = 6 - 5 = 1.
stack: [2]
answer: [1, 1, 0, 2, 1, 1, 0, 0]
stack not empty. temperatures[6] (76) > temperatures[stack.top()=2] (75).
  Pop 2. answer[2] = 6 - 2 = 4.
stack: []
answer: [1, 1, 4, 2, 1, 1, 0, 0]
Push 6.
stack: [6]
answer: [1, 1, 4, 2, 1, 1, 0, 0]

--- i = 7, temp = 73 ---
stack not empty. temperatures[7] (73) <= temperatures[stack.top()=6] (76).
Push 7.
stack: [6, 7]
answer: [1, 1, 4, 2, 1, 1, 0, 0]

End of loop. Return answer.
Final Answer: [1, 1, 4, 2, 1, 1, 0, 0]

---

## 📊 Complexity Analysis

### Time Complexity
O(n) - Each element is pushed onto the stack and popped from the stack at most once. The operations within the loop (stack push/pop, comparisons) take constant time. Therefore, the total time complexity is linear with respect to the number of temperatures.

### Space Complexity
O(n) - In the worst-case scenario (e.g., temperatures are in strictly decreasing order like [90, 80, 70, 60]), all indices will be pushed onto the stack before any are popped. This means the stack can store up to n elements, leading to O(n) space complexity.

---

## ⚠️ Edge Cases

- Array with only one element: The loop will run once, the stack will store the index, and the answer will remain [0].
- Temperatures are in strictly increasing order: Each element will cause the previous one to be popped, resulting in [1, 1, 1, ..., 1, 0].
- Temperatures are in strictly decreasing order: All indices will be pushed onto the stack, and no elements will be popped until the end (or never if the array ends). The answer will be all zeros.
- All temperatures are the same: Similar to decreasing order, the answer will be all zeros.

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
*Generated on 2025-11-27 15:06:20*
