from typing import List

class Solution:
    def solve(self, v: List[int], a: int, b: int) -> int:
        n = len(v)
        i = 0
        f = 0
        c = 0
        while i < n:
            if (f == 0 and v[i] == a) or (f == 1 and v[i] == b):
                c += 1
                f = f ^ 1
            i += 1
        return c
    
    def maximumLength(self, nums: List[int]) -> int:
        v = []
        c1 = c2 = 0
        for i in nums:
            k = i % 2
            v.append(k)
            if k == 1:
                c1 += 1
            else:
                c2 += 1
        ans = max(c1, c2)
        ans = max(ans, self.solve(v, 0, 1))
        ans = max(ans, self.solve(v, 1, 0))
        return ans