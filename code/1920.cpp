// Codes for 
//     1920. Build Array from Permutation
// Author : Yu-Cheng Lin 
//          2021. 12. 19 - version 1 
// Complexity : O(n)

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> out_ary;
        for(unsigned int i = 0, s = nums.size() ; i < s ; ++i)
            out_ary.push_back(nums[nums[i]]);
        return out_ary;
    }
};