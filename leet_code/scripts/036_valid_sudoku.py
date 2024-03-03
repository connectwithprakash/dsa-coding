# First Attempt: Brute-force O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        is_valid = True
        # row check
        idx = 0
        while is_valid and idx < m:
            data = []
            jdx = 0
            while is_valid and jdx < n:
                if board[idx][jdx] != '.':
                    if board[idx][jdx] not in data:
                        data.append(board[idx][jdx])
                    else:
                        is_valid = False
                jdx += 1
            idx += 1
        # col check
        idx = 0
        while is_valid and idx < m:
            data = []
            jdx = 0
            while is_valid and jdx < n:
                if board[jdx][idx] != '.':
                    if board[jdx][idx] not in data:
                        data.append(board[jdx][idx])
                    else:
                        is_valid = False
                jdx += 1
            idx += 1
        # 3x3 grid
        for idx in range(0, m, 3):
            for jdx in range(0, n, 3):
                kdx = 0
                data = []
                while is_valid and kdx < 3:
                    ldx = 0
                    while is_valid and ldx < 3:
                        if board[idx+kdx][jdx+ldx] != '.':
                            if board[idx+kdx][jdx+ldx] not in data:
                                data.append(board[idx+kdx][jdx+ldx])
                            else:
                                is_valid = False
                        ldx += 1
                    kdx += 1
        
        return is_valid

