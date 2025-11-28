# 645. Set Mismatch

**Difficulty:** 🟢 EASY

**Topics/Tags:** `Array`, `Hash Table`, `Math`, `Sorting`

---

## 📝 Problem Statement

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

### Example 1:

**Input:** `nums = [1,2,2,4]`
**Output:** `[2,3]`

### Example 2:

**Input:** `nums = [1,1]`
**Output:** `[1,2]`

### Constraints:

*   `2 <= nums.length <= 10^4`
*   `1 <= nums[i] <= 10^4`

### Input
An integer array `nums` representing the set of numbers after an error occurred. The original set contained numbers from `1` to `n` (where `n` is the length of `nums`).

### Output
An array of two integers. The first integer is the number that appears twice in `nums`, and the second integer is the number that is missing from the original set.

---


## 💡 Explanation

The solution first sorts the input array `nums` to easily identify the **duplicate number** by checking adjacent elements. Then, it uses a **set** to efficiently store the unique numbers present in `nums`. Finally, it iterates from 1 to `n` (where `n` is the length of `nums`) and checks for the **missing number** by seeing which number is not in the set. The duplicate and missing numbers are then returned.

---

## 🔑 Key Insights

1. The original set contained numbers from 1 to `n`. This means the sum of numbers from 1 to `n` is a known value, and the sum of the given `nums` array will differ by the amount of the missing number minus the duplicate number.
2. Sorting the array allows for a simple linear scan to find the **duplicate number** by comparing adjacent elements.
3. Using a **hash set** provides efficient O(1) average time complexity for checking the presence of a number, which is crucial for finding the missing element.
4. The problem guarantees exactly one number is duplicated and exactly one is missing, simplifying the search for these two specific values.

---

## 🎯 Hints

1. Consider how sorting the array can help you find the **repeated element**.
2. A **hash set** (or a frequency map) is a good data structure to quickly check for the existence of elements.
3. Think about the expected sum of numbers from 1 to `n` and how it relates to the sum of the given `nums` array.
4. You can iterate from 1 to `n` and check if each number is present in the input array.
5. The problem statement implies that the numbers are within a specific range (1 to `n`), which can be leveraged.
6. You need to find two specific numbers: the one that appears twice and the one that is absent.

---

## 🔍 Algorithm

```
function findErrorNums(nums):
  sort nums
  duplicate = -1
  missing = 1

  // Find the duplicate number
  for i from 1 to length(nums) - 1:
    if nums[i] == nums[i-1]:
      duplicate = nums[i]
      break

  // Create a set of numbers present in nums
  set_nums = create a new set
  for num in nums:
    add num to set_nums

  // Find the missing number
  for num from 1 to length(nums):
    if num is not in set_nums:
      missing = num
      break

  return [duplicate, missing]
```

---

## 📋 Approach

1. **Sort the input array `nums`** to bring duplicate elements together.
2. **Iterate through the sorted array** to find the duplicate number by comparing adjacent elements.
3. **Create a hash set** containing all elements from the `nums` array for efficient lookups.
4. **Iterate from 1 to `n`** (where `n` is the length of `nums`) and check if each number exists in the hash set.
5. The number that is not found in the hash set is the **missing number**.
6. **Return an array** containing the found duplicate and missing numbers.

---

## 🚶 Step-by-Step Walkthrough

Let's trace with `nums = [1, 2, 2, 4]`.

**Step 1: Sort the array**
- `nums` becomes `[1, 2, 2, 4]`.

**Step 2: Find the duplicate**
- Initialize `duplicate = -1`.
- Iterate through `nums`:
  - `i = 1`: `nums[1]` (2) is not equal to `nums[0]` (1).
  - `i = 2`: `nums[2]` (2) is equal to `nums[1]` (2). **Duplicate found!**
    - `duplicate` is set to `nums[2]`, which is `2`.
    - Break the loop.

  Current state:
  ```
  nums = [1, 2, 2, 4]
         ↑
         (comparison starts here)
  duplicate = 2
  ```

---

**Step 3: Create a set of numbers**
- Initialize `set_nums = {}`.
- Add elements from `nums` to `set_nums`:
  - Add 1: `set_nums = {1}`
  - Add 2: `set_nums = {1, 2}`
  - Add 2: `set_nums = {1, 2}` (no change as 2 is already present)
  - Add 4: `set_nums = {1, 2, 4}`

  Current state:
  ```
  set_nums = {1, 2, 4}
  ```

---

**Step 4: Find the missing number**
- Initialize `missing = 1`.
- Iterate from `num = 1` to `len(nums)` (which is 4):
  - `num = 1`: Is 1 in `set_nums`? Yes.
  - `num = 2`: Is 2 in `set_nums`? Yes.
  - `num = 3`: Is 3 in `set_nums`? No. **Missing number found!**
    - `missing` is set to `3`.
    - Break the loop.

  Current state:
  ```
  num = 3
  set_nums = {1, 2, 4}
  missing = 3
  ```

---

**Step 5: Return the result**
- Return `[duplicate, missing]`, which is `[2, 3]`.

✓ The output `[2, 3]` matches the example.

---

## 📊 Complexity Analysis

### Time Complexity
**O(n log n)** - The dominant operation is sorting the input array `nums`, which takes O(n log n) time. Creating the set takes O(n) time on average, and iterating to find the missing number takes O(n) time. Therefore, the overall time complexity is determined by the sorting step.

### Space Complexity
**O(n)** - The space complexity is primarily due to the creation of the `set_nums`. In the worst case, this set will store `n` unique elements from the input array. The sorting operation might also use some auxiliary space depending on the sorting algorithm implementation (e.g., O(log n) for quicksort or O(n) for mergesort in some implementations).

---

## ⚠️ Edge Cases

- **Array with only two elements:** e.g., `nums = [1, 1]`. The duplicate is 1, and the missing is 2. The algorithm should handle this correctly.
- **Duplicate is the smallest number:** e.g., `nums = [1, 1, 3, 4]`. Duplicate is 1, missing is 2. The sorting and set approach should work.
- **Duplicate is the largest number:** e.g., `nums = [1, 2, 3, 3]`. Duplicate is 3, missing is 4. The algorithm should handle this.
- **Missing number is 1:** e.g., `nums = [2, 2, 3, 4]`. Duplicate is 2, missing is 1. The initial `missing = 1` and the subsequent check should correctly identify this.
- **Missing number is `n`:** e.g., `nums = [1, 2, 3, 3]`. Duplicate is 3, missing is 4. The loop for finding the missing number goes up to `n`.

---

## ❌ Common Mistakes

1. **Incorrectly initializing `missing`:** If `missing` is not initialized to 1 (the smallest possible missing number), and 1 is indeed the missing number, the algorithm might fail. The provided solution correctly initializes `missing = 1`.
2. **Inefficient duplicate finding:** Without sorting, finding the duplicate might require nested loops (O(n^2)) or a hash map, which is less direct than the sorted approach for this specific problem.
3. **Not handling the `n` value correctly:** The range of numbers is from 1 to `n`, where `n` is `len(nums)`. Forgetting this can lead to incorrect bounds when searching for the missing number.
4. **Assuming numbers are unique before processing:** The core of the problem is that numbers are *not* unique. Any approach that assumes uniqueness initially will fail.

---

## 💡 Optimization Tips

1. **O(n) Time, O(n) Space using a Hash Set/Map:** Instead of sorting, you can use a hash set to find the duplicate in O(n) time. Iterate through `nums`. If a number is already in the set, it's the duplicate. Then, calculate the expected sum (n*(n+1)/2) and subtract the actual sum of `nums`. The difference will be `missing - duplicate`. You can then find the missing number: `missing = expected_sum - actual_sum + duplicate`.
2. **O(n) Time, O(1) Space using Sum and XOR:** Calculate the expected sum of numbers from 1 to `n`. Calculate the actual sum of `nums`. The difference `expected_sum - actual_sum` will be `missing - duplicate`. You can also use XOR. XOR all numbers from 1 to `n` and XOR all numbers in `nums`. The result will be `missing ^ duplicate`. With `missing - duplicate` and `missing ^ duplicate`, you can solve for `missing` and `duplicate`.
3. **O(n) Time, O(1) Space using In-place Marking (if allowed to modify input):** Treat the array indices as a hash map. For each number `num` in `nums`, go to index `abs(num) - 1`. If the number at that index is positive, make it negative. If it's already negative, `abs(num)` is the duplicate. After marking, iterate through the array again. The index `i` where `nums[i]` is still positive indicates that `i + 1` is the missing number.

---

## 📥 Examples

### Example 1
**Input:** `[1,2,2,4]`
**Output:** `[2,3]`

### Example 2
**Input:** `[1,1]`
**Output:** `[1,2]`

---
*Generated on 2025-11-28 11:38:51*
