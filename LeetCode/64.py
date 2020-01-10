class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            return sum([row[0] for row in grid])
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]

        for i in range(1, len(grid)):
            grid[i][1] += max(grid[i][0], grid[i-1][1])
        for j in range(1, len(grid[0])):
            grid[1][j] += max(grid[1][j-1], grid[0][j])

        return self.minPathSum([row[1:] for row in grid[1:])
