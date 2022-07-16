class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash_ary = [0 for t in range(2**k)]
        sum_val = int(s[0])
        if len(s) < k:
            return False
        for i in range(1,k):
            sum_val <<= 1
            sum_val += int(s[i])
        hash_ary[sum_val] = 1
        for i in range(1,len(s)-k+1):
            # print(sum_val)
            sum_val = (sum_val << 1) - int(s[i-1])*(2**k) + int(s[i+k-1])
            hash_ary[sum_val] = 1
            # print(sum_val)
        # print(hash_ary)
        return (sum(hash_ary) == 2**k)