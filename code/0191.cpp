class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t one = 1;
        int sum = 0;
        for(int i = 0 ; i < 32 ; ++i){
            if((n & one) == one) sum += 1;
            one <<= 1;
        }
        return sum;
    }
};