class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> uniq(26,0);
        for(int i = 0 ; i < s.size() ; ++i)
            ++uniq[s[i]-'a'];
        for(int i = 0 ; i < t.size() ; ++i)
            --uniq[t[i]-'a'];
        for(int i = 0 ; i < uniq.size() ; ++i)
            if(uniq[i] != 0) return false;
        return true;
        
    }
};