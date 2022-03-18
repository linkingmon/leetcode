class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> uniq(26,-2); // -2: init ; -1: repeat
        for(int i = 0 ; i < s.size() ; ++i){
            int& cur_val = uniq[s[i]-'a'];
            if(cur_val == -2) cur_val = i;
            else cur_val = -1;
        }
        int res = s.size();
        for(int i = 0 ; i < uniq.size() ; ++i)
            if(uniq[i] != -2 && uniq[i] != -1)
                res = min(uniq[i], res);
        if(res == s.size()) return -1;
        return res;
    }
};