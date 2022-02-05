class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def color_board(board,i,j):
            board[i][j] = "^"
            if i > 0 and board[i-1][j] == "O":
                color_board(board,i-1,j)
            if i < len(board)-1 and board[i+1][j] == "O":
                color_board(board,i+1,j)
            if j > 0 and board[i][j-1] == "O":
                color_board(board,i,j-1)
            if j < len(board[0])-1 and board[i][j+1] == "O":
                color_board(board,i,j+1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                color_board(board, 0, j)
            if board[len(board)-1][j] == "O":
                color_board(board, len(board)-1, j)
        for i in range(len(board)):
            if board[i][0] == "O":
                color_board(board, i, 0)
            if board[i][len(board[0])-1] == "O":
                color_board(board, i, len(board[0])-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "O" if board[i][j] == "^" else "X"