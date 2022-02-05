class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        path_ary = [[0 for t in range(len(obstacleGrid[0]))] for t in range(len(obstacleGrid))]
        block = False
        for i in range(len(obstacleGrid)):
            block = True if obstacleGrid[i][0] else block
            path_ary[i][0] = 0 if block else 1
        block = False
        for j in range(len(obstacleGrid[0])):
            block = True if obstacleGrid[0][j] == 1 else block
            path_ary[0][j] = 0 if block else 1
        
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                path_ary[i][j] = path_ary[i-1][j] + path_ary[i][j-1]
                path_ary[i][j] *= (1-obstacleGrid[i][j])
        return path_ary[-1][-1]
        