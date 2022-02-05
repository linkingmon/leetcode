class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        prod = 1
        out_val = 0
        while right < len(nums):
            prod *= nums[right]
            while prod >= k and left < right:
                prod //= nums[left]
                left += 1
            out_val += (right-left+1) if prod < k else 0
            right += 1
        
        return out_val
                