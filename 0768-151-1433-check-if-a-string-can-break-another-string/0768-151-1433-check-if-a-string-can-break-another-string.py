class Solution:
    def checkIfCanBreak(self, s: str, t: str) -> bool:
        return all(map(le,*sorted(map(sorted,(s,t)))))