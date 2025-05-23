class Solution:
    def solve(self, index1, index2, text, pattern, dp):
        if index1 < 0 and index2 < 0:
            return True
        if index2 < 0 and index1 >= 0:
            return False
        if index1 < 0 and index2 >= 0:
            for i in range(index2 + 1):
                if pattern[i] != '*':
                    return False
            return True
        if dp[index1][index2] != -1:
            return dp[index1][index2] == 1

        if text[index1] == pattern[index2] or pattern[index2] == '?':
            dp[index1][index2] = int(self.solve(index1 - 1, index2 - 1, text, pattern, dp))
        elif pattern[index2] == '*':
            dp[index1][index2] = int(self.solve(index1 - 1, index2, text, pattern, dp) or self.solve(index1, index2 - 1, text, pattern, dp))
        else:
            dp[index1][index2] = 0
        return dp[index1][index2] == 1

    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.solve(n1 - 1, n2 - 1, s, p, dp)