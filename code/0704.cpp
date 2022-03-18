class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        while(true){
            int mid = floor((start + end)/2);
            if(target == nums[mid]) return mid;
            else if(target < nums[mid]) end = mid -1;
            else start = mid + 1;
            if(end<start) return -1;
        }
    }
};