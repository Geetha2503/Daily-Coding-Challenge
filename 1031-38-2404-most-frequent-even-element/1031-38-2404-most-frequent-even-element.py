class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        map={}

        for i in nums:
            if i in map and i%2 == 0:
                map[i]+=1
            elif i not in map and i%2 == 0:
                map[i] = 1
        if len(map) == 0:
            return -1
        res = max(map,key=lambda key:map[key])
        return res