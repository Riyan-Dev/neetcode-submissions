class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal rows
        setsX = [set() for _ in range(9)]
        setsY = [set() for _ in range(9)]
        sets3x3 = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                value = int(board[i][j])
                if value in setsX[i]:
                    return False
                else:
                    setsX[i].add(value)

                if value in setsY[j]:
                    return False
                else:
                    setsY[j].add(value)

                if value in sets3x3[i//3][j//3]:
                    return False
                else:
                    sets3x3[i//3][j//3].add(value)

        return True