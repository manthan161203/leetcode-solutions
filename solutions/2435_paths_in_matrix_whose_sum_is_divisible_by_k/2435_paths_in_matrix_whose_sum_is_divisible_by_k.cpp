# Solution - CPP

#include <vector>

class Solution {
public:
    int numberOfPaths(std::vector<std::vector<int>>& grid, int k) {
        long long MOD = 1e9 + 7;
        int m = grid.size();
        int n = grid[0].size();

        // dp[i][j][r] = ways to reach cell (i,j) with remainder r
        std::vector<std::vector<std::vector<int>>> dp(m, std::vector<std::vector<int>>(n, std::vector<int>(k, 0)));

        // Base case
        int first_r = grid[0][0] % k;
        dp[0][0][first_r] = 1;

        // Fill DP table
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                int val_mod = val % k;

                // Already filled starting cell
                if (i == 0 && j == 0) {
                    continue;
                }

                for (int r = 0; r < k; ++r) {
                    // From top
                    if (i > 0 && dp[i - 1][j][r] > 0) {
                        int new_r = (r + val_mod) % k;
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i - 1][j][r]) % MOD;
                    }

                    // From left
                    if (j > 0 && dp[i][j - 1][r] > 0) {
                        int new_r = (r + val_mod) % k;
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j - 1][r]) % MOD;
                    }
                }
            }
        }

        // Answer = ways to reach last cell with remainder 0
        return dp[m - 1][n - 1][0];
    }
};
```
