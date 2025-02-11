class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []

        for numCandies in candies:
            res.append(numCandies + extraCandies >= maxCandies)
        
        return res