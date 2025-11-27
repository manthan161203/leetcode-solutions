# Daily Temperatures

**Difficulty:** 🟡 Medium

**Tags:** Array, Stack, Monotonic Stack

---

## 📝 Problem Statement
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

---

## 💡 Explanation
The problem asks us to find, for each day, how many days we need to wait to encounter a warmer temperature. If no warmer temperature exists in the future, we should report 0. This problem can be efficiently solved using a monotonic stack. A monotonic stack is a stack where the elements are always in a specific order (either strictly increasing or strictly decreasing). In this case, we'll use a decreasing monotonic stack to store the indices of days with temperatures. When we encounter a new day's temperature, we compare it with the temperature of the day at the top of the stack. If the current day's temperature is warmer, it means we've found the next warmer day for the day at the top of the stack. We pop the index from the stack, calculate the difference in days, and store it in our result array. We repeat this process until the stack is empty or the current temperature is not warmer than the top of the stack. Then, we push the current day's index onto the stack. This ensures that the stack always maintains indices of days with decreasing temperatures, allowing us to quickly find the next warmer day.

---

## 🎯 Hints
- Consider using a data structure that can efficiently keep track of previous days and their temperatures.
- A stack might be useful for this problem. Think about what you would store in the stack and how you would maintain its properties.
- Try to maintain a stack of indices where the temperatures are in decreasing order.
- When you encounter a new temperature, compare it with the temperature at the top of the stack. If it's warmer, you've found the answer for the day at the top of the stack.

---

## 🔍 Algorithm
**Monotonic Stack**

### Approach Steps
- Initialize an empty stack to store indices of days.
- Initialize a result array `answer` of the same length as `temperatures`, filled with zeros.
- Iterate through the `temperatures` array from left to right using an index `i`.
- For each day `i`, while the stack is not empty AND the temperature on day `i` is greater than the temperature on the day whose index is at the top of the stack:
-   Pop the index `idx` from the stack.
-   Calculate the number of days to wait: `i - idx`.
-   Store this difference in `answer[idx]`.
- After the while loop (either the stack is empty or the current temperature is not warmer than the top of the stack), push the current index `i` onto the stack.
- After iterating through all temperatures, return the `answer` array.

---

## 📊 Complexity
- **Time Complexity:** O(n), where n is the number of temperatures. Each element is pushed onto and popped from the stack at most once.
- **Space Complexity:** O(n) in the worst case, where n is the number of temperatures. This occurs when the temperatures are in strictly decreasing order, and all indices are pushed onto the stack.

---

## 🚶 Walkthrough
Let's trace the example: `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

Initialize `stack = []`, `n = 8`, `answer = [0, 0, 0, 0, 0, 0, 0, 0]`.

1. `i = 0`, `temperatures[0] = 73`:
   - Stack is empty. Push `0` onto stack. `stack = [0]`.

2. `i = 1`, `temperatures[1] = 74`:
   - `stack` is not empty. `temperatures[1] (74) > temperatures[stack[-1]] (temperatures[0] = 73)`.
   - Pop `0` from stack. `idx = 0`. `answer[0] = 1 - 0 = 1`. `stack = []`.
   - Stack is now empty. Push `1` onto stack. `stack = [1]`.
   - `answer = [1, 0, 0, 0, 0, 0, 0, 0]`.

3. `i = 2`, `temperatures[2] = 75`:
   - `stack` is not empty. `temperatures[2] (75) > temperatures[stack[-1]] (temperatures[1] = 74)`.
   - Pop `1` from stack. `idx = 1`. `answer[1] = 2 - 1 = 1`. `stack = []`.
   - Stack is now empty. Push `2` onto stack. `stack = [2]`.
   - `answer = [1, 1, 0, 0, 0, 0, 0, 0]`.

4. `i = 3`, `temperatures[3] = 71`:
   - `stack` is not empty. `temperatures[3] (71) <= temperatures[stack[-1]] (temperatures[2] = 75)`.
   - Push `3` onto stack. `stack = [2, 3]`.
   - `answer = [1, 1, 0, 0, 0, 0, 0, 0]`.

5. `i = 4`, `temperatures[4] = 69`:
   - `stack` is not empty. `temperatures[4] (69) <= temperatures[stack[-1]] (temperatures[3] = 71)`.
   - Push `4` onto stack. `stack = [2, 3, 4]`.
   - `answer = [1, 1, 0, 0, 0, 0, 0, 0]`.

6. `i = 5`, `temperatures[5] = 72`:
   - `stack` is not empty. `temperatures[5] (72) > temperatures[stack[-1]] (temperatures[4] = 69)`.
   - Pop `4` from stack. `idx = 4`. `answer[4] = 5 - 4 = 1`. `stack = [2, 3]`.
   - `temperatures[5] (72) > temperatures[stack[-1]] (temperatures[3] = 71)`.
   - Pop `3` from stack. `idx = 3`. `answer[3] = 5 - 3 = 2`. `stack = [2]`.
   - `temperatures[5] (72) <= temperatures[stack[-1]] (temperatures[2] = 75)`.
   - Push `5` onto stack. `stack = [2, 5]`.
   - `answer = [1, 1, 0, 2, 1, 0, 0, 0]`.

7. `i = 6`, `temperatures[6] = 76`:
   - `stack` is not empty. `temperatures[6] (76) > temperatures[stack[-1]] (temperatures[5] = 72)`.
   - Pop `5` from stack. `idx = 5`. `answer[5] = 6 - 5 = 1`. `stack = [2]`.
   - `temperatures[6] (76) > temperatures[stack[-1]] (temperatures[2] = 75)`.
   - Pop `2` from stack. `idx = 2`. `answer[2] = 6 - 2 = 4`. `stack = []`.
   - Stack is now empty. Push `6` onto stack. `stack = [6]`.
   - `answer = [1, 1, 4, 2, 1, 1, 0, 0]`.

8. `i = 7`, `temperatures[7] = 73`:
   - `stack` is not empty. `temperatures[7] (73) <= temperatures[stack[-1]] (temperatures[6] = 76)`.
   - Push `7` onto stack. `stack = [6, 7]`.
   - `answer = [1, 1, 4, 2, 1, 1, 0, 0]`.

End of iteration. Return `answer = [1, 1, 4, 2, 1, 1, 0, 0]`.

---

## ⚠️ Edge Cases
- Empty input array: The problem constraints state `1 <= temperatures.length`, so an empty array is not possible.
- Array with all same temperatures: e.g., `[30, 30, 30]`. The output should be `[0, 0, 0]`.
- Array with strictly increasing temperatures: e.g., `[30, 40, 50]`. The output should be `[1, 1, 0]`.
- Array with strictly decreasing temperatures: e.g., `[50, 40, 30]`. The output should be `[0, 0, 0]`.
- Single element array: e.g., `[70]`. The output should be `[0]`.

Generated on 2025-11-27 12:56:36.128918
