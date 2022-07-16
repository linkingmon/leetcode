class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_row = len(matrix)
        n_col = len(matrix[0])
        self.par_sum = matrix.copy();
        for i in range(n_row):
            row_sum = 0
            for j in range(n_col):
                row_sum += matrix[i][j]
                self.par_sum[i][j] = self.par_sum[i-1][j] + row_sum if i != 0 else row_sum
        print(self.par_sum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans1 = self.par_sum[row1-1][col1-1] if row1 != 0 and col1 != 0 else 0
        ans2 = self.par_sum[row1-1][col2] if row1 != 0 else 0
        ans3 = self.par_sum[row2][col1-1] if col1 != 0 else 0
        ans4 = self.par_sum[row2][col2]
        return ans4 + ans1 - ans2 - ans3


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)