class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perimeter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i < row - 1 and grid[i+1][j] == 1:
                        perimeter -= 2
                    if j < col - 1 and grid[i][j+1] == 1:
                        perimeter -= 2


        return perimeter
        