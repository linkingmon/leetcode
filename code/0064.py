class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_ary = [[0 for t in range(len(grid[0]))] for t in range(len(grid))]
        sum_val = 0
        for i in range(len(grid)):
            sum_val += grid[i][0]
            min_ary[i][0] = sum_val
        sum_val = 0
        for j in range(len(grid[0])):
            sum_val += grid[0][j]
            min_ary[0][j] = sum_val
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                min_ary[i][j] = min(min_ary[i-1][j],min_ary[i][j-1]) + grid[i][j]
        return min_ary[-1][-1]