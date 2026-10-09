class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        def dfs(cur,i,j,a, path):
            nonlocal found

            if (i, j) in path:
                return False

            if "".join(cur) == word:
                found = True
                return True

            if i >= len(board) or j >= len(board[i]):
                return False
            if i < 0 or j < 0:
                return False

    
            if word[a] == board[i][j]:
                cur.append(board[i][j])

                path.append((i, j))
                c1 = dfs(cur, i+1, j, a+1, path)
                c2 = dfs(cur, i, j+1, a+1, path)
                c3 = dfs(cur, i-1, j, a+1, path)
                c4 = dfs(cur, i, j-1, a+1, path)
                cur.pop()
                path.pop()
                if c1 or c2 or c3 or c4: return True

        for i in range(len(board)):
            for j in range (len(board[i])):
                if board[i][j] == word[0]:
                    dfs([], i, j, 0, [])
                    if found: return True
        
        return False

