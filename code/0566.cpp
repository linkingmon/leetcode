class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        if(mat.size()*mat[0].size() != r*c) return mat;
        int i = 0;
        int cur_row = 0;
        int cur_col = 0;
        vector<vector<int>> res;
        vector<int> tmp(c);
        while(true){
            tmp[i] = mat[cur_row][cur_col];
            if(cur_col == mat[0].size()-1){
                cur_col = 0;
                ++cur_row;
            }
            else ++cur_col;
            if(i == c-1){
                res.push_back(tmp);
                if(res.size() == r) break;
                i = 0;
            }
            else ++i;
        }
        return res;
    }
};