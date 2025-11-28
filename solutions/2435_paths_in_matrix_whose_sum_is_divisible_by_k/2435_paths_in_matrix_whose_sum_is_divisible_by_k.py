# Solution - PYTHON

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][r] = ways to reach cell (i,j) with remainder r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Base case
        first_r = grid[0][0] % k
        dp[0][0][first_r] = 1
        
        # Fill DP table
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                val_mod = val % k
                
                # Already filled starting cell
                if i == 0 and j == 0:
                    continue
                
                for r in range(k):
                    # From top
                    if i > 0 and dp[i-1][j][r] > 0:
                        new_r = (r + val_mod) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                    
                    # From left
                    if j > 0 and dp[i][j-1][r] > 0:
                        new_r = (r + val_mod) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD
        
        # Answer = ways to reach last cell with remainder 0
        return dp[m-1][n-1][0]

