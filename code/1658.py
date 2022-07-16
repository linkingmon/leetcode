class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # suffix map
        cur_sum = nums[-1]
        suffix_hash = {x:0, (x-cur_sum):1}
        for i in range(len(nums)-2,-1,-1):
            cur_sum += nums[i]
            suffix_hash[x-cur_sum] = len(nums) - i
        # prefix sum
        cur_sum = 0
        min_val = suffix_hash[cur_sum] if cur_sum in suffix_hash else len(nums) + 1
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_val = suffix_hash[cur_sum] if cur_sum in suffix_hash else len(nums) + 1
            min_val = min(min_val,cur_val+i+1)
        return min_val if (min_val != len(nums) + 1) else -1