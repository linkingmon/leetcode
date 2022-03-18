class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res;
        res.reserve(nums.size());
        int start = 0, end = nums.size()-1;
        while(start<=end){
            if(abs(nums[start]) > abs(nums[end]))
                res.push_back(nums[start]*nums[start++]);
            else
                res.push_back(nums[end]*nums[end--]);
        }
        reverse(res.begin(),res.end());
        return res;
    }
};