class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums) // 2]
        return sum([abs(num-med) for num in nums])
