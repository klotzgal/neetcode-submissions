class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_sets = [set() for _ in range(len(board))]
        
        for i in range(len(board)):
            row_set = set()
            if i % 3 == 0:
                box_sets = [set() for _ in range(3)]

            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in row_set or board[i][j] in column_sets[j] or board[i][j] in box_sets[j // 3]:
                        return False
                    else:
                        row_set.add(board[i][j])
                        column_sets[j].add(board[i][j])
                        box_sets[j // 3].add(board[i][j])

        return True
