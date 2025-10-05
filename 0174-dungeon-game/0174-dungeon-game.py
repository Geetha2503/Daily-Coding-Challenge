class Solution:
    def solve(self, i, j, dungeon, dp):
        m, n = len(dungeon), len(dungeon[0])

        # Base case: Bottom-right cell (princess's room)
        if i == m - 1 and j == n - 1:
            return max(1, 1 - dungeon[i][j])

        # If out of bounds
        if i >= m or j >= n:
            return float('inf')

        # If the value is already calculated
        if dp[i][j] != -1:
            return dp[i][j]

        # Recursive calculation for the minimum health needed
        right = self.solve(i, j + 1, dungeon, dp)
        down = self.solve(i + 1, j, dungeon, dp)

        # The knight needs at least 1 health point to survive
        min_health = min(right, down) - dungeon[i][j]
        dp[i][j] = max(1, min_health)

        return dp[i][j]

    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        # Create a memoization table initialized with -1
        dp = [[-1] * n for _ in range(m)]

        # Start from the top-left cell
        return self.solve(0, 0, dungeon, dp)