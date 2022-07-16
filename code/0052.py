class Solution:
    def totalNQueens(self, n: int) -> int:
        sol = []
        def backtrack(cur_sol, row):
            if len(cur_sol) == n and row == n:
                sol.append(cur_sol)
                print(sol)
            for col in range(n):
                if all(row != row1 and col != col1 and abs(row - row1) != abs(col - col1) for row1, col1 in cur_sol):
                    backtrack(cur_sol + [(row, col)], row + 1)
        backtrack([],0)
        return len(sol)