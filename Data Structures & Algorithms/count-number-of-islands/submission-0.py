class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[i]):
                return 
            if i < 0 or j < 0:
                return
            if grid[i][j] != "1":
                return
            
            grid[i][j] = "X"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b] == "1":
                    count += 1
                    dfs(a, b)

        return count