class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visited, prevH):
            if (i < 0 or j < 0 or 
                i >= ROWS or j >= COLS or
                heights[i][j] < prevH or
                (i, j) in visited): return
            
            visited.add((i, j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i,j) in atl:
                    res.append((i, j))

        return res

                


