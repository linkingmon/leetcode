class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_val = n*(n+1) // 2
        for i in range(n):
            sum_val -= nums[i]
        return sum_val