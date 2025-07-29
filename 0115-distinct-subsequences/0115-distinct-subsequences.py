class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m)]for _ in range(n)]

        def count_match(i, j):
            if j < 0:
                return 1 
            elif i < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = count_match(i-1, j-1) + count_match(i-1, j)
            else:
                dp[i][j] = count_match(i-1, j)

            return dp[i][j]
        
        return count_match(n-1, m-1)