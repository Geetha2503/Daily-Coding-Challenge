class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        height: [1, 0, 1, 2, 4, 2,6]
                 left            right
       TC: O(n) 
       SC: O(1)
        
        
        
        '''
        
    
        if not height or len(height) < 3:
            return 0  # If less than 3 elements, water cannot be trapped

        left, right = 0, len(height) - 1  # Two pointers at both ends
        max_left, max_right = height[left], height[right]  # Track max heights
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:  # Process smaller height side
                left += 1  # Move left pointer
                max_left = max(max_left, height[left])  # Update max_left
                water_trapped += max_left - height[left]  # Water trapped at left
            else:
                right -= 1  # Move right pointer
                max_right = max(max_right, height[right])  # Update max_right
                water_trapped += max_right - height[right]  # Water trapped at right

        return water_trapped
