class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        while(true){
            if(end-start==1) return target > nums[end] ? end + 1 : target > nums[start] ? end : start;
            if(end==start) return target > nums[end] ? end + 1 : end;
            int mid = floor((start + end)/2);
            if(target == nums[mid]) return mid;
            else if(target < nums[mid]) end = mid - 1;
            else start = mid + 1;
        }
    }
};