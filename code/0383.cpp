class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> uniq(26,0);
        for(int i = 0 ; i < magazine.size() ; ++i)
            ++uniq[magazine[i]-'a'];
        for(int i = 0 ; i < ransomNote.size() ; ++i)
            --uniq[ransomNote[i]-'a'];
        for(int i = 0 ; i < uniq.size() ; ++i)
            if(uniq[i] < 0) return false;
        return true;
    }
};