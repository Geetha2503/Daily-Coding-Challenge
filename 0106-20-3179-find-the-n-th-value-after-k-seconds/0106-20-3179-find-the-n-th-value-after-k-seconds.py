class Solution:
    def valueAfterKSeconds(self, n: int, k: int, ans = 1) -> int:

        for i in range(min(k, n-1)):
            ans = ans * (k+n-1 - i)//(i+1)

        return ans  %1_000_000_007