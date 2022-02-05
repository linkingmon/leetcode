class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col_num = len(matrix[0])
        row_vector = matrix[0]
        is_toeplitz = True
        for i in range(1,len(matrix)):
            next_vector = [matrix[i][0]] + row_vector
            next_vector.pop()
            for j in range(col_num):
                is_toeplitz = is_toeplitz and (next_vector[j] == matrix[i][j])
            if is_toeplitz == False:
                return False
            row_vector = next_vector
        return True
        