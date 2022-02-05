class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        s = 0 
        m = 2**maximumBit-1
        for i in range(len(nums)):
            s = s^nums[i]
        out_list = []
        for i in range(len(nums)-1,-1,-1):
            out_list.append(s^m)
            s = s^nums[i]
        return out_list