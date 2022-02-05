class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        max_ary = [[-inf for t in range(len(grid[0]))] for t2 in range(len(grid))]
        min_ary = [[inf for t in range(len(grid[0]))] for t2 in range(len(grid))]
        cur_mult = 1
        for i in range(len(grid[0])):
            cur_mult = cur_mult * grid[0][i]
            if cur_mult >= 0:
                max_ary[0][i] = cur_mult
            if cur_mult <= 0:
                min_ary[0][i] = cur_mult
        cur_mult = 1
        for i in range(len(grid)):
            cur_mult = cur_mult * grid[i][0]
            if cur_mult >= 0:
                max_ary[i][0] = cur_mult
            if cur_mult <= 0:
                min_ary[i][0] = cur_mult
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                # if grid[]
                max_path = max(max_ary[i-1][j],max_ary[i][j-1])
                min_path = min(min_ary[i-1][j],min_ary[i][j-1])
                max_ary[i][j] = grid[i][j]*max_path if grid[i][j] > 0 else 0 if grid[i][j] == 0 else grid[i][j]*min_path
                min_ary[i][j] = grid[i][j]*min_path if grid[i][j] > 0 else 0 if grid[i][j] == 0 else grid[i][j]*max_path
                

        res = max_ary[len(grid)-1][len(grid[0])-1]%1000000007
        return res if res >= 0 else -1