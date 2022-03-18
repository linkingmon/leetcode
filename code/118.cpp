class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        res.push_back(vector<int>(1,1));
        for(int i = 1 ; i < numRows ; ++i){
            vector<int> tmp(i+1);
            tmp[0] = 1;
            for(int j = 1 ; j < i ; ++j) tmp[j] = res[i-1][j-1] + res[i-1][j];
            tmp[i] = 1;
            res.push_back(tmp);
        }
        return res;
    }
};