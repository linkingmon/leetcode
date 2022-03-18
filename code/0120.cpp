class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> ans;
        for(int i = 0 ; i < triangle.size() ; ++i) ans.push_back(vector<int>(triangle.size(),0));
        ans[0][0] = triangle[0][0];
        for(int i = 1 ; i < triangle.size() ; ++i){
            ans[i][0] = ans[i-1][0] + triangle[i][0];
            for(int j = 1 ; j < i ; ++j)
                ans[i][j] = min(ans[i-1][j-1],ans[i-1][j]) + triangle[i][j];
            ans[i][i] = ans[i-1][i-1] + triangle[i][i];
        }
        int res = ans[triangle.size()-1][0];
        for(int i = 1 ; i < triangle.size() ; ++i)
            res = min(res,ans[triangle.size()-1][i]);
        return res;
    }
};