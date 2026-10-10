class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = collections.deque()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    q.append((i, j))

        while q:

            for _ in range(len(q)):

                i, j = q.popleft()
                toCheck = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

                for (a,b) in toCheck:
                    if a >= len(grid) or b >= len(grid[a]) or a < 0 or b < 0:
                        continue

                    if grid[a][b] != 2147483647: continue

                    grid[a][b] = grid[i][j] + 1
                    q.append((a, b))

            
            
            

