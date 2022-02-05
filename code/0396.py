class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sum_prod = 0
        sum_val = sum(nums)
        for i in range(1,len(nums)):
            sum_prod += (nums[i]*i)
        out_val = sum_prod
        for i in range(len(nums)-1):
            sum_prod -= sum_val
            sum_prod += nums[i]*len(nums)
            out_val = max(sum_prod,out_val)
        return out_val
            