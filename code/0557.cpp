class Solution {
public:
    string reverseWords(string s) {
        int start = 0, end;
        bool cut = false;
        s = s + ' ';
        for(int i = 0 ; i < s.size() ; ++i){
            if(s[i] == ' '){
                cut = true;
                end = i - 1;
                reverse(s,start,end);
            }
            else{
                if(cut == true) start = i;
                cut = false;
            }
        }
        return s.substr(0,s.size()-1);
    }
    void reverse(string& s, int start, int end){
        while(start < end){
            swap(s[start++],s[end--]);
        }
    }
};