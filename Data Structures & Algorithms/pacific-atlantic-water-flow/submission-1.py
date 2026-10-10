class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = False
        atl = False
        res = []

        def dfs(i, j, visited, h):
            nonlocal pac, atl
            if (i, j) in visited: return
            # for pacific
            if i < 0 or j <0:
                pac = True
                return
            # for atlantic
            if i >= len(heights) or j >= len(heights[i]):
                atl = True
                return
            if heights[i][j] > h:
                return
            visited.append((i, j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                dfs(i, j, [], heights[i][j])
                if pac and atl: res.append([i, j])
                pac = False
                atl = False

        return res
