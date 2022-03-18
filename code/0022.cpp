class Solution {
public:
    int n_pair;
    vector<string> generateParenthesis(int n) {
        n_pair = n;
        vector<string> ans;
        trace(ans, "", 0, 0);
        return ans;
    }
    void trace(vector<string>& ans, string s, int open, int left){
        if(s.size() == 2*n_pair) { ans.push_back(s); return; }
        if(open != 0) trace(ans, s+')', open-1, left);
        if(open != n_pair && left != n_pair) trace(ans, s+'(', open+1, left+1);
    }
};