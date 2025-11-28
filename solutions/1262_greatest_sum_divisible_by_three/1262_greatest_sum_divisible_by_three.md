# 1262. Greatest Sum Divisible by Three

**Difficulty:** 🟡 MEDIUM

**Topics/Tags:** `Array`, `Dynamic Programming`, `Greedy`

---

## 📝 Problem Statement

Given an integer array `nums`, return the maximum possible sum of elements of the array such that it is divisible by three.

### Example 1:

**Input:** `nums = [3,6,5,1,8]`
**Output:** `18`
**Explanation:** Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

### Example 2:

**Input:** `nums = [4]`
**Output:** `0`
**Explanation:** Since 4 is not divisible by 3, do not pick any number.

### Example 3:

**Input:** `nums = [1,2,3,4,4]`
**Output:** `12`
**Explanation:** Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

### Constraints:

*   `1 <= nums.length <= 4 * 10^4`
*   `1 <= nums[i] <= 10^4`

### Input
An array of integers `nums`.

### Output
The maximum possible sum of elements from `nums` that is divisible by three.

---


## 💡 Explanation

This solution finds the maximum sum of elements in `nums` that is divisible by three. It first calculates the total sum and checks if it's already divisible by three. If not, it identifies the smallest numbers to remove to make the sum divisible by three, based on the remainder of the total sum. The core idea is to leverage **modular arithmetic** to efficiently determine the necessary adjustments.

---

## 🔑 Key Insights

1. The problem can be solved by considering the **remainder of the total sum when divided by 3**.
2. If the total sum is divisible by 3, that's the maximum possible sum. Otherwise, we need to remove elements such that the remaining sum is divisible by 3.
3. To minimize the removed sum (and thus maximize the remaining sum), we should remove the **smallest possible numbers** that adjust the total sum's remainder to 0.
4. If the total sum has a remainder of 1, we either remove one number with remainder 1, or two numbers with remainder 2. We choose the option that removes the smallest sum.
5. If the total sum has a remainder of 2, we either remove one number with remainder 2, or two numbers with remainder 1. We choose the option that removes the smallest sum.

---

## 🎯 Hints

1. Calculate the **total sum** of all elements in `nums` first.
2. Check the **remainder of the total sum when divided by 3**.
3. If the total sum is not divisible by 3, you need to remove elements. Consider the **remainders of individual numbers** when divided by 3.
4. To maximize the sum, you want to remove the **smallest possible sum** of elements that corrects the remainder.
5. Sort the numbers based on their **remainders modulo 3** to easily find the smallest ones.
6. Handle cases where there aren't enough numbers with specific remainders to perform a removal (e.g., needing two numbers with remainder 2 but only having one).

---

## 🔍 Algorithm

```
function maxSumDivThree(nums):
    total_sum = sum(nums)

    if total_sum % 3 == 0:
        return total_sum

    # Separate numbers based on their remainder modulo 3
    nums_rem_0 = []
    nums_rem_1 = []
    nums_rem_2 = []
    for num in nums:
        if num % 3 == 0:
            nums_rem_0.append(num)
        elif num % 3 == 1:
            nums_rem_1.append(num)
        else: # num % 3 == 2
            nums_rem_2.append(num)

    # Sort lists to easily pick smallest elements
    nums_rem_1.sort()
    nums_rem_2.sort()

    min_removal = float('inf')

    if total_sum % 3 == 1:
        # Option 1: Remove one number with remainder 1
        if len(nums_rem_1) >= 1:
            min_removal = min(min_removal, nums_rem_1[0])
        # Option 2: Remove two numbers with remainder 2
        if len(nums_rem_2) >= 2:
            min_removal = min(min_removal, nums_rem_2[0] + nums_rem_2[1])
    else: # total_sum % 3 == 2
        # Option 1: Remove one number with remainder 2
        if len(nums_rem_2) >= 1:
            min_removal = min(min_removal, nums_rem_2[0])
        # Option 2: Remove two numbers with remainder 1
        if len(nums_rem_1) >= 2:
            min_removal = min(min_removal, nums_rem_1[0] + nums_rem_1[1])

    # If no valid removal is possible, the max sum divisible by 3 is 0 (empty set)
    if min_removal == float('inf'):
        return 0

    return total_sum - min_removal

```

---

## 📋 Approach

1. Calculate the **sum of all elements** in the input array `nums`.
2. Check if the `total_sum` is **divisible by 3**. If it is, return `total_sum` as it's the maximum possible sum.
3. If `total_sum` is not divisible by 3, we need to remove elements. Separate the numbers in `nums` into three lists based on their **remainder when divided by 3**: `nums_rem_0`, `nums_rem_1`, and `nums_rem_2`.
4. **Sort** `nums_rem_1` and `nums_rem_2` in ascending order. This allows us to easily pick the smallest numbers with specific remainders.
5. Determine the **minimum sum to remove** based on the `total_sum % 3`:
6.   - If `total_sum % 3 == 1`: Consider removing the smallest number from `nums_rem_1` OR the sum of the two smallest numbers from `nums_rem_2`.
7.   - If `total_sum % 3 == 2`: Consider removing the smallest number from `nums_rem_2` OR the sum of the two smallest numbers from `nums_rem_1`.
8. Keep track of the **minimum removal sum** found. If a required removal (e.g., two numbers with remainder 2) is not possible due to insufficient elements, treat its removal sum as infinity.
9. If `min_removal` remains infinity after considering all options, it means no combination of removals can make the sum divisible by 3, so return 0 (representing an empty selection).
10. Otherwise, return `total_sum - min_removal`.

---

## 🚶 Step-by-Step Walkthrough

Let's walk through `nums = [3, 6, 5, 1, 8]`

**Step 1:** Calculate the total sum.
```
total_sum = 3 + 6 + 5 + 1 + 8 = 23
```

**Step 2:** Check if `total_sum` is divisible by 3.
```
23 % 3 = 2
```
It's not divisible by 3. We need to remove elements.

**Step 3:** Separate numbers by remainder modulo 3.
```
nums_rem_0: [3, 6]
nums_rem_1: [1]
nums_rem_2: [5, 8]
```

**Step 4:** Sort `nums_rem_1` and `nums_rem_2`.
```
nums_rem_1: [1]
nums_rem_2: [5, 8]
```
(Already sorted in this case)

**Step 5:** Determine minimum removal sum.
Since `total_sum % 3 == 2`, we have two options:

*   **Option A: Remove one number with remainder 2.**
    The smallest number in `nums_rem_2` is `5`.
    Removal sum = `5`.

*   **Option B: Remove two numbers with remainder 1.**
    We need at least two numbers in `nums_rem_1`. We only have one (`1`).
    This option is not possible. We can represent its removal sum as `infinity`.

Now, compare the possible removal sums:
```
min_removal = min(5, infinity) = 5
```

**Step 6:** Calculate the final maximum sum.
```
max_sum = total_sum - min_removal
max_sum = 23 - 5 = 18
```

**Result:** 18

--- 

Let's walk through `nums = [1, 2, 3, 4, 4]`

**Step 1:** Calculate the total sum.
```
total_sum = 1 + 2 + 3 + 4 + 4 = 14
```

**Step 2:** Check if `total_sum` is divisible by 3.
```
14 % 3 = 2
```
It's not divisible by 3. We need to remove elements.

**Step 3:** Separate numbers by remainder modulo 3.
```
nums_rem_0: [3]
nums_rem_1: [1, 4, 4]
nums_rem_2: [2]
```

**Step 4:** Sort `nums_rem_1` and `nums_rem_2`.
```
nums_rem_1: [1, 4, 4]
nums_rem_2: [2]
```

**Step 5:** Determine minimum removal sum.
Since `total_sum % 3 == 2`, we have two options:

*   **Option A: Remove one number with remainder 2.**
    The smallest number in `nums_rem_2` is `2`.
    Removal sum = `2`.

*   **Option B: Remove two numbers with remainder 1.**
    The two smallest numbers in `nums_rem_1` are `1` and `4`.
    Removal sum = `1 + 4 = 5`.

Now, compare the possible removal sums:
```
min_removal = min(2, 5) = 2
```

**Step 6:** Calculate the final maximum sum.
```
max_sum = total_sum - min_removal
max_sum = 14 - 2 = 12
```

**Result:** 12


---

## 📊 Complexity Analysis

### Time Complexity
**O(N log N)** - The dominant factor is sorting the `nums_rem_1` and `nums_rem_2` lists. In the worst case, all numbers could fall into one of these lists, leading to a sort operation on up to N elements. Summing the array takes O(N), and partitioning takes O(N). Therefore, the overall time complexity is O(N log N) due to sorting.

### Space Complexity
**O(N)** - In the worst-case scenario, all numbers in the input array `nums` could have remainders of 1 or 2 modulo 3. This would result in `nums_rem_1` and `nums_rem_2` lists storing up to N elements combined. Therefore, the space complexity is O(N) to store these auxiliary lists.

---

## ⚠️ Edge Cases

- **Array with a single element**: The code handles this by checking `len(nums) == 1` and returning the element if divisible by 3, otherwise 0.
- **All numbers are divisible by 3**: The `total_sum` will be divisible by 3, and the function will correctly return `total_sum`.
- **No combination of numbers sums to a multiple of 3**: If after considering removals, `min_removal` remains `infinity`, the function correctly returns 0.
- **Insufficient numbers for removal**: For example, if `total_sum % 3 == 1` and `nums_rem_2` has fewer than 2 elements, or `nums_rem_1` has fewer than 1 element. The code handles this by using `float('inf')` for impossible removal options.
- **Large input array**: The constraints allow for `nums.length` up to 4 * 10^4. The O(N log N) time complexity and O(N) space complexity are acceptable for these constraints.

---

## 📥 Examples

### Example 1
**Input:** `[3,6,5,1,8]`
**Output:** `18`

### Example 2
**Input:** `[4]`
**Output:** `0`

### Example 3
**Input:** `[1,2,3,4,4]`
**Output:** `12`

---
*Generated on 2025-11-28 12:11:55*
