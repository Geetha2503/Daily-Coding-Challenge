class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n, l = len(s), len(s) // k
        c1 = Counter(s[i:i+l] for i in range(0,n,l))
        c2 = Counter(t[i:i+l] for i in range(0,n,l))
        return c1 == c2