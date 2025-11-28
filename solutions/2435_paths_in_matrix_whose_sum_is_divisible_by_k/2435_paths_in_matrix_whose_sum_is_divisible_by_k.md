# 2435. Paths in Matrix Whose Sum Is Divisible by K

**Difficulty:** 🔴 HARD

**Topics/Tags:** `Dynamic Programming`, `Array`

---

## 📝 Problem Statement

You are given a 0-indexed `m x n` integer matrix `grid` and an integer `k`. You are currently at position `(0, 0)` and you want to reach position `(m - 1, n - 1)` moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by `k`. Since the answer may be very large, return it modulo `10^9 + 7`.

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

This problem is solved using **dynamic programming**. We maintain a 3D DP table where `dp[i][j][r]` stores the number of paths to reach cell `(i, j)` such that the sum of elements along the path has a **remainder `r` when divided by `k`**. The core idea is that the number of paths to a cell depends on the number of paths to its top and left neighbors, considering the remainder of the current cell's value.

---

## 🔑 Key Insights

1. The problem can be solved efficiently by focusing on the **remainders modulo k** of path sums, rather than the actual sums, which can become very large.
2. A **dynamic programming** approach is suitable because the problem has optimal substructure (paths to a cell depend on paths to previous cells) and overlapping subproblems (the same subpaths are calculated multiple times).
3. The state of our DP needs to include not just the cell coordinates `(i, j)` but also the **remainder of the path sum modulo k** to make decisions about future paths.
4. We can transition from a cell `(i, j)` to its neighbors `(i+1, j)` and `(i, j+1)`. Conversely, to calculate `dp[i][j][r]`, we consider paths coming from `(i-1, j)` and `(i, j-1)`.

---

## 🎯 Hints

1. Think about how the **remainder of a sum** changes when you add a new number. Specifically, `(a + b) % k = ((a % k) + (b % k)) % k`.
2. Use a **3D DP table** where dimensions represent row, column, and the remainder modulo k.
3. The **base case** is the starting cell `(0, 0)`. Initialize its DP state based on its value modulo k.
4. When calculating the DP state for `dp[i][j][new_r]`, consider the states from `dp[i-1][j]` and `dp[i][j-1]`. The `new_r` will be `(previous_remainder + current_cell_value) % k`.
5. Remember to apply the **modulo operation (10^9 + 7)** at each addition to prevent integer overflow.
6. The final answer will be the value in `dp[m-1][n-1][0]`, representing paths to the bottom-right cell with a sum divisible by k (remainder 0).

---

## 🔍 Algorithm

```
function numberOfPaths(grid, k):
    MOD = 10^9 + 7
    m = length of grid
    n = length of grid[0]

    // dp[i][j][r] = number of paths to reach cell (i, j) with path sum % k == r
    dp = array of size m x n x k, initialized to 0

    // Base case: starting cell (0, 0)
    initial_remainder = grid[0][0] % k
    dp[0][0][initial_remainder] = 1

    // Iterate through the grid
    for i from 0 to m-1:
        for j from 0 to n-1:
            current_val = grid[i][j]
            current_val_mod = current_val % k

            // If it's the starting cell, we've already handled it
            if i == 0 and j == 0:
                continue

            // Calculate DP states for current cell (i, j)
            for r from 0 to k-1:
                // Paths coming from the cell above (i-1, j)
                if i > 0:
                    // If there are paths to (i-1, j) with remainder r
                    if dp[i-1][j][r] > 0:
                        new_remainder = (r + current_val_mod) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i-1][j][r]) % MOD

                // Paths coming from the cell to the left (i, j-1)
                if j > 0:
                    // If there are paths to (i, j-1) with remainder r
                    if dp[i][j-1][r] > 0:
                        new_remainder = (r + current_val_mod) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i][j-1][r]) % MOD

    // The answer is the number of paths to the bottom-right cell (m-1, n-1) with remainder 0
    return dp[m-1][n-1][0]
```

---

## 📋 Approach

1. **Initialize DP Table**: Create a 3D DP table `dp[m][n][k]` filled with zeros. `dp[i][j][r]` will store the count of paths to cell `(i, j)` with a path sum modulo `k` equal to `r`.
2. **Set Base Case**: For the starting cell `(0, 0)`, calculate its value modulo `k`. Set `dp[0][0][grid[0][0] % k]` to 1, as there's one way to reach the start with that initial remainder.
3. **Iterate Through Grid**: Traverse the grid row by row, and column by column.
4. **Calculate Transitions**: For each cell `(i, j)` and for each possible remainder `r` (from 0 to `k-1`):
5.   - **From Top**: If `i > 0`, consider paths coming from `(i-1, j)`. If `dp[i-1][j][r]` is greater than 0, it means there are `dp[i-1][j][r]` paths to `(i-1, j)` with remainder `r`. Add `grid[i][j]` to these paths. The new remainder will be `(r + grid[i][j]) % k`. Update `dp[i][j][(r + grid[i][j]) % k]` by adding `dp[i-1][j][r]` (modulo `MOD`).
6.   - **From Left**: If `j > 0`, consider paths coming from `(i, j-1)`. If `dp[i][j-1][r]` is greater than 0, update `dp[i][j][(r + grid[i][j]) % k]` by adding `dp[i][j-1][r]` (modulo `MOD`).
7. **Return Result**: After filling the DP table, the answer is `dp[m-1][n-1][0]`, which represents the number of paths to the destination cell `(m-1, n-1)` with a path sum divisible by `k` (i.e., remainder 0).

---

## 🚶 Step-by-Step Walkthrough

Let's walk through Example 1: `grid = [[5,2,4],[3,0,5],[0,7,2]]`, `k = 3`.

`m = 3`, `n = 3`, `k = 3`. `MOD = 10^9 + 7`.

Initialize `dp[3][3][3]` with all zeros.

**Step 1: Base Case (0, 0)**
- `grid[0][0] = 5`. `5 % 3 = 2`.
- `dp[0][0][2] = 1`.

DP Table (showing only non-zero entries for clarity, `dp[row][col][remainder]`):
```
dp[0][0][2] = 1
```

--- 

**Step 2: Cell (0, 1)**
- `grid[0][1] = 2`. `2 % 3 = 2`.
- **From Left (0, 0)**:
  - `dp[0][0][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 2) % 3 = 4 % 3 = 1`.
  - `dp[0][1][1] = (dp[0][1][1] + dp[0][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
dp[0][0][2] = 1
dp[0][1][1] = 1
```

--- 

**Step 3: Cell (0, 2)**
- `grid[0][2] = 4`. `4 % 3 = 1`.
- **From Left (0, 1)**:
  - `dp[0][1][1] = 1`. Previous remainder `r = 1`.
  - `new_remainder = (1 + 1) % 3 = 2 % 3 = 2`.
  - `dp[0][2][2] = (dp[0][2][2] + dp[0][1][1]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
dp[0][0][2] = 1
dp[0][1][1] = 1
dp[0][2][2] = 1
```

--- 

**Step 4: Cell (1, 0)**
- `grid[1][0] = 3`. `3 % 3 = 0`.
- **From Top (0, 0)**:
  - `dp[0][0][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 0) % 3 = 2 % 3 = 2`.
  - `dp[1][0][2] = (dp[1][0][2] + dp[0][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
dp[0][0][2] = 1
dp[0][1][1] = 1
dp[0][2][2] = 1
dp[1][0][2] = 1
```

--- 

**Step 5: Cell (1, 1)**
- `grid[1][1] = 0`. `0 % 3 = 0`.
- **From Top (0, 1)**:
  - `dp[0][1][1] = 1`. Previous remainder `r = 1`.
  - `new_remainder = (1 + 0) % 3 = 1 % 3 = 1`.
  - `dp[1][1][1] = (dp[1][1][1] + dp[0][1][1]) % MOD = (0 + 1) % MOD = 1`.
- **From Left (1, 0)**:
  - `dp[1][0][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 0) % 3 = 2 % 3 = 2`.
  - `dp[1][1][2] = (dp[1][1][2] + dp[1][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
dp[0][0][2] = 1
dp[0][1][1] = 1
dp[0][2][2] = 1
dp[1][0][2] = 1
dp[1][1][1] = 1
dp[1][1][2] = 1
```

--- 

**Step 6: Cell (1, 2)**
- `grid[1][2] = 5`. `5 % 3 = 2`.
- **From Top (0, 2)**:
  - `dp[0][2][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 2) % 3 = 4 % 3 = 1`.
  - `dp[1][2][1] = (dp[1][2][1] + dp[0][2][2]) % MOD = (0 + 1) % MOD = 1`.
- **From Left (1, 1)**:
  - `dp[1][1][1] = 1`. Previous remainder `r = 1`.
  - `new_remainder = (1 + 2) % 3 = 3 % 3 = 0`.
  - `dp[1][2][0] = (dp[1][2][0] + dp[1][1][1]) % MOD = (0 + 1) % MOD = 1`.
  - `dp[1][1][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 2) % 3 = 4 % 3 = 1`.
  - `dp[1][2][1] = (dp[1][2][1] + dp[1][1][2]) % MOD = (1 + 1) % MOD = 2`.

DP Table:
```
...
dp[1][2][0] = 1
dp[1][2][1] = 2
```

--- 

**Step 7: Cell (2, 0)**
- `grid[2][0] = 0`. `0 % 3 = 0`.
- **From Top (1, 0)**:
  - `dp[1][0][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 0) % 3 = 2 % 3 = 2`.
  - `dp[2][0][2] = (dp[2][0][2] + dp[1][0][2]) % MOD = (0 + 1) % MOD = 1`.

DP Table:
```
...
dp[2][0][2] = 1
```

--- 

**Step 8: Cell (2, 1)**
- `grid[2][1] = 7`. `7 % 3 = 1`.
- **From Top (1, 1)**:
  - `dp[1][1][1] = 1`. Previous remainder `r = 1`.
  - `new_remainder = (1 + 1) % 3 = 2 % 3 = 2`.
  - `dp[2][1][2] = (dp[2][1][2] + dp[1][1][1]) % MOD = (0 + 1) % MOD = 1`.
  - `dp[1][1][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 1) % 3 = 3 % 3 = 0`.
  - `dp[2][1][0] = (dp[2][1][0] + dp[1][1][2]) % MOD = (0 + 1) % MOD = 1`.
- **From Left (2, 0)**:
  - `dp[2][0][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 1) % 3 = 3 % 3 = 0`.
  - `dp[2][1][0] = (dp[2][1][0] + dp[2][0][2]) % MOD = (1 + 1) % MOD = 2`.

DP Table:
```
...
dp[2][1][0] = 2
dp[2][1][2] = 1
```

--- 

**Step 9: Cell (2, 2) - Destination**
- `grid[2][2] = 2`. `2 % 3 = 2`.
- **From Top (1, 2)**:
  - `dp[1][2][0] = 1`. Previous remainder `r = 0`.
  - `new_remainder = (0 + 2) % 3 = 2 % 3 = 2`.
  - `dp[2][2][2] = (dp[2][2][2] + dp[1][2][0]) % MOD = (0 + 1) % MOD = 1`.
  - `dp[1][2][1] = 2`. Previous remainder `r = 1`.
  - `new_remainder = (1 + 2) % 3 = 3 % 3 = 0`.
  - `dp[2][2][0] = (dp[2][2][0] + dp[1][2][1]) % MOD = (0 + 2) % MOD = 2`.
- **From Left (2, 1)**:
  - `dp[2][1][0] = 2`. Previous remainder `r = 0`.
  - `new_remainder = (0 + 2) % 3 = 2 % 3 = 2`.
  - `dp[2][2][2] = (dp[2][2][2] + dp[2][1][0]) % MOD = (1 + 2) % MOD = 3`.
  - `dp[2][1][2] = 1`. Previous remainder `r = 2`.
  - `new_remainder = (2 + 2) % 3 = 4 % 3 = 1`.
  - `dp[2][2][1] = (dp[2][2][1] + dp[2][1][2]) % MOD = (0 + 1) % MOD = 1`.

Final DP Table (relevant entries for (2,2)):
```
dp[2][2][0] = 2
dp[2][2][1] = 1
dp[2][2][2] = 3
```

**Result**: The answer is `dp[m-1][n-1][0] = dp[2][2][0] = 2`.

This matches the example output.

---

## 📊 Complexity Analysis

### Time Complexity
**O(m * n * k)**. We iterate through each cell of the `m x n` grid. For each cell, we iterate through all `k` possible remainders. Inside the innermost loop, operations are constant time. Therefore, the total time complexity is proportional to `m * n * k`.

### Space Complexity
**O(m * n * k)**. We use a 3D DP table of size `m x n x k` to store the number of paths for each cell and each remainder. This table dominates the space usage.

---

## ⚠️ Edge Cases

- **Grid of size 1x1**: If `m=1` and `n=1`, the answer is 1 if `grid[0][0] % k == 0`, and 0 otherwise. The DP correctly handles this as the base case is the destination.
- **k = 1**: If `k` is 1, any sum is divisible by 1. The number of paths will be the total number of paths from `(0,0)` to `(m-1, n-1)` in a grid, which is `C(m+n-2, m-1)`. The DP will correctly compute this as every remainder will be 0.
- **All elements in grid are 0**: If all `grid[i][j]` are 0, the path sum will always be 0. If `k > 0`, then `0 % k == 0`. The DP will correctly count all possible paths.
- **Large values in grid**: The problem constraints state `grid[i][j] <= 100`. While individual values are small, the sum can grow large. The use of modulo `k` at each step prevents overflow issues with path sums.
- **Maximum grid dimensions**: `m, n <= 5 * 10^4` and `m * n <= 5 * 10^4`. This implies that either `m` or `n` (or both) can be large, but the total number of cells is limited. The DP approach is efficient enough given this constraint on `m*n`.

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
*Generated on 2025-11-28 14:41:33*
