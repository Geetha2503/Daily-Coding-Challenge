class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
    
        nums.sort()
        maxDiff = 0

        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, nums[i] - nums[i - 1])
    
        return maxDiff