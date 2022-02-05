class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n_ones = sum(nums)
        nums = nums + nums[0:n_ones-1]
        sum_val = sum(nums[0:n_ones])
        min_swap = n_ones - sum_val
        for i in range(n_ones,len(nums)):
            sum_val = sum_val + nums[i] - nums[i-n_ones]
            if (n_ones - sum_val) < min_swap:
                min_swap = n_ones - sum_val
        return min_swap