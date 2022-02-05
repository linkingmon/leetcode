// Codes for 
//     3. Longest Substring Without Repeating Characters
// Author : Yu-Cheng Lin 
//          2021. 12. 25 - version 1 
// Complexity : O(n)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int str_len = s.size();
        int max_len = 0;
        int unique[256];
        for(int i = 0 ; i < 256 ; ++i) unique[i] = -1;
        int l = 0;
        for(int r = 0 ; r < str_len ; ++r){
            if(unique[int(s[r])] != -1) l = max(l, unique[int(s[r])]+1);
            unique[int(s[r])] = r;
            if(r-l+1 > max_len) max_len = r-l+1;
        }
        return max_len;
    }
};