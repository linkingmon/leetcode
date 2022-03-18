class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> char_count(26,0);
        int end = 0;
        for(int i = 0 ; i < s1.size() ; ++i) 
            char_count[s1[i]-'a'] += 1;
        while(end < s2.size()){
            if(end >= s1.size()) char_count[s2[end-s1.size()]-'a'] += 1;
            char_count[s2[end]-'a'] -= 1;
            bool all_zero = true;
            for(int i = 0 ; i < 26 ; ++i) if(char_count[i] != 0) all_zero = false;
            if(all_zero) return true;
            ++end;
        }
        return false;   
    }
};