class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        vector<vector<bool>> colored;
        for(int i = 0 ; i < grid.size() ; ++i)
            colored.push_back(vector<bool>(grid[0].size(),false));
        int max_area = 0;
        for(int i = 0 ; i < grid.size() ; ++i){
            for(int j = 0 ; j < grid[0].size() ; ++j){
                int area = 0;
                if(!colored[i][j]) color(i,j,grid,colored,area);
                max_area = max(max_area,area);
            }
        }    
        return max_area;
    }
   void color(int sr, int sc, vector<vector<int>>& grid, vector<vector<bool>>& colored, int& area){
        if(!colored[sr][sc] && grid[sr][sc]==1){
            colored[sr][sc] = true;
            area += 1;
        }
        else return;
        if(sr-1>=0) color(sr-1, sc, grid, colored, area);
        if(sr+1<grid.size()) color(sr+1, sc, grid, colored, area);
        if(sc-1>=0) color(sr, sc-1, grid, colored, area);
        if(sc+1<grid[0].size()) color(sr, sc+1, grid, colored, area);
    }
};