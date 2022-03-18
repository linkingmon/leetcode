class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t one = 1;
        uint32_t one_reverse = (1 << 31);
        for(int i = 0 ; i < 16 ; ++i){
            bool one_val = (n & one) == one;
            bool one_reverse_val = (n & one_reverse) == one_reverse;
            if(one_val) n |= one_reverse;
            else n &= (~one_reverse);
            if(one_reverse_val) n |= one;
            else n &= (~one);
            one <<= 1;
            one_reverse >>= 1;
        }
        return n;
        
    }
};