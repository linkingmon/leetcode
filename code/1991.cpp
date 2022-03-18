class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int right_val = 0;
        for(int i = 1 ; i < nums.size() ; ++i)
            right_val += nums[i];
        int left_val = 0;
        if(left_val == right_val) return 0;
        for(int i = 1 ; i < nums.size() ; ++i){
            left_val += nums[i-1];
            right_val -= nums[i];
            if(left_val == right_val) return i;
        }
        return -1;
    }
};