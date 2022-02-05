// Codes for 
//     1. Two Sum
// Author : Yu-Cheng Lin 
//          2021. 12. 19 - version 1 
// Complexity : O(nlgn) Sort + O(n) search

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> idx_ary(nums.size());
        std::iota(idx_ary.begin(),idx_ary.end(),0);
        sort(idx_ary.begin(),idx_ary.end(), [&](int i,int j){return nums[i]<nums[j];} ); 
        sort(nums.begin(), nums.end());
        int pivot_1, pivot_2;
        for(pivot_2 = nums.size()-1 ; ; --pivot_2)
            if(2*nums[pivot_2] <= target) break;
        for(pivot_1 = 0 ; ; ++pivot_1) 
            if(2*nums[pivot_1] >= target) break;
        if(pivot_1 == pivot_2) --pivot_1;
        while(1){
            int sum = nums[pivot_1] + nums[pivot_2];
            if(sum > target) --pivot_1;
            else if(sum < target) ++pivot_2;
            else break;
        }
        vector<int> out_ary{idx_ary[pivot_1], idx_ary[pivot_2]};
        return out_ary;
    }
};