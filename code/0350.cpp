class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        multiset<int> mset;
        vector<int> res;
        for(int i = 0 ; i < nums1.size() ; ++i) mset.insert(nums1[i]);
        for(int i = 0 ; i < nums2.size() ; ++i){
            multiset<int>::iterator it = mset.find(nums2[i]);
            if(it != mset.end()){
                res.push_back(*it);
                mset.erase(it);
            }
        }
        return res;
    }
};