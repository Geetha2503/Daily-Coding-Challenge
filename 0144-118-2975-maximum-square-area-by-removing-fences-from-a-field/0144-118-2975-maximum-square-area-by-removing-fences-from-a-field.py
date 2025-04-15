class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        hFences.sort()
        vFences.sort()

        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        ans = -1
        cnt = {}

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                cnt[hFences[j] - hFences[i]] = 1

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                if (vFences[j] - vFences[i]) in cnt:
                    ans = max(ans, vFences[j] - vFences[i])

        if ans == -1:
            return ans

        mod = 10**9 + 7
        return (ans * ans) % mod

