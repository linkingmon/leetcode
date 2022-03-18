class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = 0;
        int p2 = 0;
        int i = 0;
        vector<int> res(m+n,0);
        while(p1 != m || p2 != n){
            if(!(p1 != m && p2 == n) && ((p1 == m && p2 != n) || nums1[p1] > nums2[p2])) res[i++] = nums2[p2++];
            else res[i++] = nums1[p1++];
        }
        nums1 = res;
    }
};