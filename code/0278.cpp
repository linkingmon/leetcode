// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long int start = 1;
        long int end = n;
        while(true){
            int mid = floor((start+end)/2);
            if(isBadVersion(mid)) end = mid;
            else if(mid == start) return mid + 1;
            else start = mid;
            if(start == end) return start;
        }
    }
};