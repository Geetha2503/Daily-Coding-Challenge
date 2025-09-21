# Use two divide (/) to get floor/integer value after division
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s , e = 0 , len (nums) - 1 
        while s < e :
            m = s + (e - s ) // 2 
            if nums[m] == nums[s] and nums[m] == nums[e] :
                s += 1
                e -= 1
            elif nums[m] <= nums[e] :  e = m 
            else  :      s = m + 1 
        return nums [s] 