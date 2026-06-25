class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or it's water ('0'), stop exploring
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # Mark the current cell as visited by turning it to water
            grid[r][c] = "0"
            
            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                # When we find land, we've discovered a new island
                if grid[r][c] == "1":
                    count += 1
                    # Sink the entire island using DFS
                    dfs(r, c)
                    
        return count