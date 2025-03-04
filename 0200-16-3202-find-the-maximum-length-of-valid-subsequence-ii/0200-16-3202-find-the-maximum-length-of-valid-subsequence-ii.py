class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        maxi = 1
        for num in nums:
            currNum = num % k
            for mod in range(k):
                prevNum = (mod - currNum + k) % k
                dp[currNum][mod] = max(dp[currNum][mod] , 1 + dp[prevNum][mod])
                maxi = max(maxi , dp[currNum][mod])
        return maxi