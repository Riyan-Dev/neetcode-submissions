class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j))
        time = 0
        while q:
            for _ in range(len(q)):

                i, j = q.popleft()

                to_check = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

                for a, b in to_check:
                    if a >= len(grid) or b >= len(grid[a]) or a < 0 or b < 0:
                        continue
                    if grid[a][b] == 0 or grid[a][b] == 2:
                        continue
                    
                    grid[a][b] = 2
                    q.append((a, b))


            if q: time += 1
            
                

        for row in grid:
            if 1 in row:
                return -1
        return time

                    
