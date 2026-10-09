class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[i]):
                return 0
            if i < 0 or j < 0:
                return 0
            if grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            a = dfs(i+1, j)
            b = dfs(i, j+1)
            c = dfs(i-1, j)
            d = dfs(i, j-1)
            return a+b+c+d+1

        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b] == 1:
                    area = dfs(a, b)
                    res = max(area, res)


        return res            