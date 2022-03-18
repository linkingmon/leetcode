class Solution {
public:
    void solve(int ind, string s,vector<string>&ans){
        if (ind == s.size()){ // approach end
            ans.push_back(s);
            return;
        }
        if(s[ind] >= '0' && s[ind] <= '9') {
            solve(ind+1,s,ans);
        }
        else if(s[ind] >= 'a' && s[ind] <= 'z'){
            solve(ind+1,s,ans);
            s[ind] -= 32;
            solve(ind+1,s,ans);
        }
        else{
            solve(ind+1,s,ans);
            s[ind] += 32;
            solve(ind+1,s,ans);
        }
    }
    
    vector<string> letterCasePermutation(string s) {
        vector<string>ans;
        solve(0,s,ans);
        return ans;
    }
};