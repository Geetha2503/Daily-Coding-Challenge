class Solution:
    def minimumCost(self, nums):
        nums.sort()
        midIndex = len(nums) // 2

        def check_palindrome(x):
            x = str(x)
            return x == x[::-1]
        
        # function to calculate result
        def add(nums, target):
            result = 0
            for elem in nums:
                result += abs(elem - target)
            return result

        # finding median
        if len(nums) % 2 == 1:
            mid = nums[midIndex]
            if check_palindrome(mid):
                return add(nums, mid)
        else:
            mid = (nums[midIndex] + nums[midIndex - 1]) // 2
            if check_palindrome(mid):
                return add(nums, mid)

        p_1 = mid + 1
        p_2 = mid - 1

        # we are finding 2 palindrome, one less than other greater than median element
        while not (check_palindrome(p_1) and check_palindrome(p_2)):
            if not check_palindrome(p_1):
                p_1 += 1
            if not check_palindrome(p_2):
                p_2 -= 1

        return min(add(nums, p_1), add(nums, p_2))