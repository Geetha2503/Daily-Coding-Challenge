class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1, n + 1)))
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        result = []
        for i in range(n, 0, -1):
            idx = k // factorial[i - 1]
            result.append(nums.pop(idx))
            k %= factorial[i - 1]
        return "".join(result)