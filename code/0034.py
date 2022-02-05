class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums: List[int], start_idx, end_idx, target) -> int:
            print(start_idx,end_idx)
            if end_idx - start_idx < 2 and (target not in nums[start_idx:end_idx+1]):
                return -1 
            mid_idx = (start_idx + end_idx) // 2
            mid_val = nums[mid_idx]
            if mid_val > target:
                return search(nums, start_idx, mid_idx-1, target)
            elif mid_val < target:
                return search(nums, mid_idx+1, end_idx, target)
            else:
                return mid_idx
        start_idx = end_idx = search(nums,0,len(nums)-1,target)
        if start_idx == -1:
            return [-1,-1]
        while start_idx >= 0 and nums[start_idx] == target:
            start_idx = start_idx - 1
        while end_idx < len(nums) and nums[end_idx] == target:
            end_idx = end_idx + 1
        return [start_idx+1,end_idx-1]