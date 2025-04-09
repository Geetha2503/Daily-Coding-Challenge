class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        return all(grid[i] == grid[0] or grid[i] == [1-val for val in grid[0]] for i in range(len(grid)))