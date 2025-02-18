class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        nums1: [1,3]
        nums2: [2]    # merge: [1,2,3]  output: 2
        
        nums1: [1,3]
        nums2: [2,5,7,8]  # merge: [1,2,3,5,7,8]  output: (3+5)//2 = 4
        
        nums1: [0, 1, 1, 4, 6, 6, 7, 8]
        nums2: [1,2,2,2,4,4,4,4,4, 6]  #merge: [0]  output: 0     
        
        for merging o(m+n), taking the median value it takes o(1)
        tc: o(m+n), sc: o(m+n)
        
        Binary search - TC: O(log(m+n)) SC: O(1)
        
        i+j =(m+n) //2 (for even total length)
        i+j =(m+n+1) //2 (for odd total length)
        
        nums1[i-1] <= nums2[j]  (if i>0)
        nums2[j-1] <= nums1[i]  (if j>0)
        
        if odd: max(nums[i-1], nums2[j-1])
        if even: (max(nums[i-1], nums2[j-1])+min(nums[i], nums2[jj]))//2
        
        '''
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Partitioning nums1 at index i and nums2 at index j
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i  # Ensuring left half size matches right half

            # Elements just before and after partition
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                right = i - 1  # Move left
            else:
                left = i + 1  # Move right

        return -1  # Should not reach here
        
        
        
