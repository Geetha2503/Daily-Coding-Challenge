class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # dimensions:
        NR = len(grid)
        NC = len(grid[0])
        vec = [0] * NR * NC #initialize the vector.
        # If k is greater than the length of vector, 
		# the shift will repeat itself in a cycle; 
		# hence, we only care about the remainder.
        k = k % (NR * NC)
		
        #step 1: put the matrix row by row to the vector.
        for i in range(NR):
            for j in range(NC):
                vec[i * NC + j] = grid[i][j]
				
        #step 2: rotate vector k times by reverse approach.
        self.Rev(vec, 0, NR * NC - 1) #reverse all elements.
        self.Rev(vec, 0, k-1)       #reverse first k elements.
        self.Rev(vec, k, NR * NC - 1) #revere last len(vec)-k elements. 
        
        #step 3: put the vector to the matrix back the same way.
        for i in range(NR):
            for j in range(NC):
                grid[i][j] = vec[i * NC + j]
        return grid
		
    # This function returns the reverse a subset of the vector,
	# bound by "left" and "right" elements
    def Rev(self, vec, left, right):
        while left < right:
            vec[left], vec[right] = vec[right], vec[left]
            left += 1 
            right -= 1
        