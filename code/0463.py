class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n_col = len(grid)
        n_row = len(grid[0])
        
        ans = 0
        for i_col in range(n_col):
            if grid[i_col][0] == 1:
                ans += 1
            for i_row in range(n_row-1):
                if ((grid[i_col][i_row] == 1) ^ (grid[i_col][i_row+1] == 1)):
                    ans += 1
            if grid[i_col][n_row-1] == 1:
                ans += 1
                
        for i_row in range(n_row):
            if grid[0][i_row] == 1:
                ans += 1
            for i_col in range(n_col-1):
                if ((grid[i_col][i_row] == 1) ^ (grid[i_col+1][i_row] == 1)):
                    ans += 1
            if grid[n_col-1][i_row] == 1:
                ans += 1
        return ans