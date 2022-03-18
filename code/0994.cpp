class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        deque<pair<int,int>> list;
        int fresh = 0;
        for(int i = 0 ; i < grid.size() ; ++i)
            for(int j = 0 ; j < grid[0].size() ; ++j){
                if(grid[i][j] == 2) list.push_back(make_pair(i,j));
                if(grid[i][j] == 1) ++fresh;
            }
        vector<int> dx{-1,0,0,1};
        vector<int> dy{0,-1,1,0};
        int cnt = 0;
        while(list.size() > 0){
            int len = list.size();
            // cout << "Iter " << cnt << endl;
            for(int k = 0 ; k < len ; ++k){
                pair<int,int> point = list.front();
                // cout << "POP " << point.first << " " << point.second << endl;
                for(int i = 0 ; i < 4 ; ++i){
                    int x = point.first + dx[i];
                    int y = point.second + dy[i];
                    if(x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size()){
                        // cout << "   CHECK " << x << " " << y << endl;
                        if(grid[x][y] == 1){
                            list.push_back(make_pair(x,y));
                            grid[x][y] = 2;
                            --fresh;
                            // cout << "   PUSH " << endl;
                        }
                    }
                }
                list.pop_front();
            }
            ++cnt;
        }
        // cout << fresh;
        if(fresh != 0) return -1;
        if(cnt == 0) return 0;
        return --cnt;
    }
};