class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> num_set;
        for(int i = 0 ; i < nums.size() ; ++i)
            if(num_set.find(nums[i]) != num_set.end())
                return true;
            else
                num_set.insert(nums[i]);
        return false;
    }
};