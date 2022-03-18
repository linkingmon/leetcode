class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int point = nums.size()-1;
        int min_val = 101;
        int idx;
        while(point > 0 && nums[point-1] >= nums[point]) --point;
        if(point != 0){
            for(int i = point ; i < nums.size() ; ++i) 
                if(nums[i] > nums[point-1] && min_val > nums[i]){
                    min_val = nums[i];
                    idx = i;
                }
            swap(nums[point-1],nums[idx]);
        }
        sort(nums.begin()+point,nums.end());
    }
};