class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int ans = 0;
        int n = grid.size();
        int m = grid[0].size();
        for(int i=0; i<n; i++)
            color(grid,i,0), color(grid,i,m-1);
        for(int j=0; j<m; j++)
            color(grid,0,j), color(grid,n-1,j);
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                if(!grid[i][j])
                    color(grid,i,j), ++ans;
        return ans;
    }
    
    void color(vector<vector<int>>& grid, int i, int j) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size() || grid[i][j])
            return;
        grid[i][j] = 1;
        color(grid,i-1,j);
        color(grid,i,j-1);
        color(grid,i+1,j);
        color(grid,i,j+1);
    }
};