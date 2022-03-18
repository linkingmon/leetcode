class Solution {
public:
    vector <int> ans;
    vector <bool> calculate;
    int rob(vector<int>& nums) {
        int n = nums.size();
        ans = vector<int>(n,0);
        calculate = vector<bool>(n,false);
        return rob_sub(nums, n-1);
    }
    int rob_sub(vector<int>& nums, int n) {
        if(n == 0) return nums[0];
        if(n == 1) return max(nums[0],nums[1]);
        int step_1, step_2, val;
        if(calculate[n-1]) 
            step_1 = ans[n-1];
        else{
            step_1 = rob_sub(nums, n-1);
            ans[n-1] = step_1;
            calculate[n-1] = true;
        }
        if(calculate[n-2]) 
            step_2 = ans[n-2];
        else{
            step_2 = rob_sub(nums, n-2);
            ans[n-2] = step_1;
            calculate[n-2] = true;
        }
        val = max(step_1, step_2+nums[n]);
        calculate[n] = true;
        ans[n] = val;
        return val;
    }
};