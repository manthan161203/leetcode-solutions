# 2435. Paths in Matrix Whose Sum Is Divisible by K

**Difficulty:** 🔴 HARD

**Topics/Tags:** `Dynamic Programming`, `Array`

---

## 📝 Problem Statement

You are given a 0-indexed `m x n` integer matrix `grid` and an integer `k`.

You are currently at position `(0, 0)` and you want to reach position `(m - 1, n - 1)` moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by `k`.

Since the answer may be very large, return it modulo `10^9 + 7`.

### Example 1:

**Input:**
```
grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
```

**Output:**
```
2
```

**Explanation:**
There are two paths where the sum of the elements on the path is divisible by `k`.

The first path highlighted in red has a sum of `5 + 2 + 4 + 5 + 2 = 18` which is divisible by `3`.
The second path highlighted in blue has a sum of `5 + 3 + 0 + 5 + 2 = 15` which is divisible by `3`.

### Example 2:

**Input:**
```
grid = [[0,0]], k = 5
```

**Output:**
```
1
```

**Explanation:**
The path highlighted in red has a sum of `0 + 0 = 0` which is divisible by `5`.

### Example 3:

**Input:**
```
grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
```

**Output:**
```
10
```

**Explanation:**
Every integer is divisible by `1` so the sum of the elements on every possible path is divisible by `k`.

### Constraints:

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 5 * 10^4`
*   `1 <= m * n <= 5 * 10^4`
*   `0 <= grid[i][j] <= 100`
*   `1 <= k <= 50`

### Input
A 0-indexed `m x n` integer matrix `grid` and an integer `k`.

### Output
The number of paths from `(0, 0)` to `(m - 1, n - 1)` moving only down or right, where the sum of elements on the path is divisible by `k`, modulo `10^9 + 7`.

---

## 💡 Explanation

This solution uses **dynamic programming** to count paths in a grid where the sum of elements is divisible by `k`. The core idea is to maintain a DP table `dp[i][j][r]` representing the number of ways to reach cell `(i, j)` with a path sum that has a **remainder `r`** when divided by `k`. We build this table iteratively, considering paths coming from the top and left, and updating the remainders accordingly.

---

## 🎯 Hints

1. Think about how the **remainder** of a sum changes when you add a new number.
2. This problem can be solved using **dynamic programming** by building up solutions for subproblems.
3. The state of your DP should capture not just the position but also the **accumulated sum's remainder**.
4. Consider the transitions: a cell `(i, j)` can be reached from `(i-1, j)` (down) or `(i, j-1)` (right).
5. Remember to apply the **modulo operation** at each addition to prevent integer overflow and keep track of the count.
6. The final answer will be the count of paths reaching the bottom-right cell with a **remainder of 0**.

---

## 🔍 Algorithm

```
function numberOfPaths(grid, k):
  MOD = 10^9 + 7
  m = number of rows in grid
  n = number of columns in grid

  // dp[i][j][r] stores the number of ways to reach cell (i, j) 
  // such that the sum of elements on the path has a remainder r when divided by k.
  dp = array of size m x n x k, initialized to 0

  // Base case: Starting cell (0, 0)
  first_remainder = grid[0][0] % k
  dp[0][0][first_remainder] = 1

  // Iterate through the grid
  for i from 0 to m-1:
    for j from 0 to n-1:
      current_value = grid[i][j]
      current_remainder = current_value % k

      // If it's the starting cell, we've already handled it
      if i == 0 and j == 0:
        continue

      // Consider paths coming from the cell above (i-1, j)
      if i > 0:
        for prev_remainder from 0 to k-1:
          if dp[i-1][j][prev_remainder] > 0:
            new_remainder = (prev_remainder + current_remainder) % k
            dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i-1][j][prev_remainder]) % MOD

      // Consider paths coming from the cell to the left (i, j-1)
      if j > 0:
        for prev_remainder from 0 to k-1:
          if dp[i][j-1][prev_remainder] > 0:
            new_remainder = (prev_remainder + current_remainder) % k
            dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i][j-1][prev_remainder]) % MOD

  // The answer is the number of ways to reach the bottom-right cell (m-1, n-1) 
  // with a path sum that has a remainder of 0.
  return dp[m-1][n-1][0]
```

---

## 📋 Approach

1. Initialize a 3D DP table `dp[m][n][k]` where `dp[i][j][r]` stores the number of paths to reach cell `(i, j)` with a sum whose remainder modulo `k` is `r`.
2. Set the **base case**: For the starting cell `(0, 0)`, `dp[0][0][grid[0][0] % k]` is 1, as there's one way to reach it with that initial remainder.
3. Iterate through the grid row by row, and column by column.
4. For each cell `(i, j)`, calculate the **remainder of the current cell's value** modulo `k`.
5. For each possible previous remainder `r` (from 0 to `k-1`):
6.   If `i > 0` (meaning we can come from the cell above), update `dp[i][j][(r + current_remainder) % k]` by adding `dp[i-1][j][r]`. Apply modulo `10^9 + 7`.
7.   If `j > 0` (meaning we can come from the cell to the left), update `dp[i][j][(r + current_remainder) % k]` by adding `dp[i][j-1][r]`. Apply modulo `10^9 + 7`.
8. The final answer is `dp[m-1][n-1][0]`, which represents the number of paths to the bottom-right cell with a sum divisible by `k` (remainder 0).

---

## 🚶 Step-by-Step Walkthrough

Let's trace with `grid = [[5, 2], [3, 0]]` and `k = 3`.

`m = 2`, `n = 2`, `k = 3`.
`MOD = 10^9 + 7`.

Initialize `dp[2][2][3]` with all zeros.

**Step 1: Initialize Base Case**

- Current cell: `(0, 0)`
- `grid[0][0] = 5`
- `5 % 3 = 2`
- `dp[0][0][2] = 1`

DP Table (showing only non-zero entries for clarity):
```
(0,0): {2: 1}
```

--- 

**Step 2: Process Cell (0, 1)**

- Current cell: `(0, 1)`
- `grid[0][1] = 2`
- `2 % 3 = 2`

- **From left (0, 0):**
  - `dp[0][0]` has `remainder 2` with `count 1`.
  - `new_remainder = (2 + 2) % 3 = 4 % 3 = 1`.
  - `dp[0][1][1] = (dp[0][1][1] + dp[0][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
(0,0): {2: 1}
(0,1): {1: 1}
```

--- 

**Step 3: Process Cell (1, 0)**

- Current cell: `(1, 0)`
- `grid[1][0] = 3`
- `3 % 3 = 0`

- **From top (0, 0):**
  - `dp[0][0]` has `remainder 2` with `count 1`.
  - `new_remainder = (2 + 0) % 3 = 2`.
  - `dp[1][0][2] = (dp[1][0][2] + dp[0][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
(0,0): {2: 1}
(0,1): {1: 1}
(1,0): {2: 1}
```

--- 

**Step 4: Process Cell (1, 1)**

- Current cell: `(1, 1)`
- `grid[1][1] = 0`
- `0 % 3 = 0`

- **From top (0, 1):**
  - `dp[0][1]` has `remainder 1` with `count 1`.
  - `new_remainder = (1 + 0) % 3 = 1`.
  - `dp[1][1][1] = (dp[1][1][1] + dp[0][1][1]) % MOD = (0 + 1) % MOD = 1`.

- **From left (1, 0):**
  - `dp[1][0]` has `remainder 2` with `count 1`.
  - `new_remainder = (2 + 0) % 3 = 2`.
  - `dp[1][1][2] = (dp[1][1][2] + dp[1][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
(0,0): {2: 1}
(0,1): {1: 1}
(1,0): {2: 1}
(1,1): {1: 1, 2: 1}
```

--- 

**Step 5: Final Result**

- The target cell is `(m-1, n-1)`, which is `(1, 1)`.
- We need the count for remainder `0`.
- `dp[1][1][0] = 0`.

Wait, let's recheck the example `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`. The output is 2.

Let's re-trace with the provided example: `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`.

`m = 3`, `n = 3`, `k = 3`.

`dp[3][3][3]` initialized to 0.

**Base Case (0,0):** `grid[0][0] = 5`, `5 % 3 = 2`. `dp[0][0][2] = 1`.

**Cell (0,1):** `grid[0][1] = 2`, `2 % 3 = 2`.
  - From (0,0) with rem 2: `(2 + 2) % 3 = 1`. `dp[0][1][1] += dp[0][0][2] = 1`.

**Cell (0,2):** `grid[0][2] = 4`, `4 % 3 = 1`.
  - From (0,1) with rem 1: `(1 + 1) % 3 = 2`. `dp[0][2][2] += dp[0][1][1] = 1`.

**Cell (1,0):** `grid[1][0] = 3`, `3 % 3 = 0`.
  - From (0,0) with rem 2: `(2 + 0) % 3 = 2`. `dp[1][0][2] += dp[0][0][2] = 1`.

**Cell (1,1):** `grid[1][1] = 0`, `0 % 3 = 0`.
  - From (0,1) with rem 1: `(1 + 0) % 3 = 1`. `dp[1][1][1] += dp[0][1][1] = 1`.
  - From (1,0) with rem 2: `(2 + 0) % 3 = 2`. `dp[1][1][2] += dp[1][0][2] = 1`.

**Cell (1,2):** `grid[1][2] = 5`, `5 % 3 = 2`.
  - From (0,2) with rem 2: `(2 + 2) % 3 = 1`. `dp[1][2][1] += dp[0][2][2] = 1`.
  - From (1,1) with rem 1: `(1 + 2) % 3 = 0`. `dp[1][2][0] += dp[1][1][1] = 1`.
  - From (1,1) with rem 2: `(2 + 2) % 3 = 1`. `dp[1][2][1] += dp[1][1][2] = 1`.
  So, `dp[1][2]` is `{0: 1, 1: 2}`.

**Cell (2,0):** `grid[2][0] = 0`, `0 % 3 = 0`.
  - From (1,0) with rem 2: `(2 + 0) % 3 = 2`. `dp[2][0][2] += dp[1][0][2] = 1`.

**Cell (2,1):** `grid[2][1] = 7`, `7 % 3 = 1`.
  - From (1,1) with rem 1: `(1 + 1) % 3 = 2`. `dp[2][1][2] += dp[1][1][1] = 1`.
  - From (1,1) with rem 2: `(2 + 1) % 3 = 0`. `dp[2][1][0] += dp[1][1][2] = 1`.
  - From (2,0) with rem 2: `(2 + 1) % 3 = 0`. `dp[2][1][0] += dp[2][0][2] = 1`.
  So, `dp[2][1]` is `{0: 2, 2: 1}`.

**Cell (2,2):** `grid[2][2] = 2`, `2 % 3 = 2`.
  - From (1,2) with rem 0: `(0 + 2) % 3 = 2`. `dp[2][2][2] += dp[1][2][0] = 1`.
  - From (1,2) with rem 1: `(1 + 2) % 3 = 0`. `dp[2][2][0] += dp[1][2][1] = 2`.
  - From (2,1) with rem 0: `(0 + 2) % 3 = 2`. `dp[2][2][2] += dp[2][1][0] = 2`.
  - From (2,1) with rem 2: `(2 + 2) % 3 = 1`. `dp[2][2][1] += dp[2][1][2] = 1`.
  So, `dp[2][2]` is `{0: 2, 1: 1, 2: 3}`.

**Final Answer:** `dp[2][2][0] = 2`.

This matches the example output. The two paths are:
1. 5 -> 2 -> 4 -> 5 -> 2 (Sum = 18, 18 % 3 = 0)
2. 5 -> 3 -> 0 -> 5 -> 2 (Sum = 15, 15 % 3 = 0)

---

## 📊 Complexity Analysis

### Time Complexity
**O(m * n * k)**. We iterate through each cell of the `m x n` grid. For each cell, we iterate through all `k` possible remainders to calculate the new remainders and update the DP table. Therefore, the total time complexity is proportional to the product of these three factors.

### Space Complexity
**O(m * n * k)**. We use a 3D DP table of size `m x n x k` to store the number of paths for each cell and each possible remainder. This table dominates the space usage.

---

## ⚠️ Edge Cases

- Grid with only one cell (`m=1, n=1`).
- Grid where `k=1`. In this case, every path sum is divisible by 1, so the answer is the total number of paths.
- Grid containing only zeros.
- Grid where `m * n` is small but `k` is large (e.g., `m=2, n=2, k=50`).
- Grid where `m * n` is large but `k` is small (e.g., `m=5000, n=10, k=2`).

---

## 📥 Examples

### Example 1
**Input:** `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`
**Output:** `2`

### Example 2
**Input:** `grid = [[0,0]], k = 5`
**Output:** `1`

### Example 3
**Input:** `grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1`
**Output:** `10`

---
*Generated on 2025-11-27 17:34:57*
