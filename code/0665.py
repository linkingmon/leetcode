class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        diff = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if (i < len(nums)-1 and nums[i-1] > nums[i+1]) and (i > 1 and nums[i-2] > nums[i]):
                    return False
                diff = diff + 1
            if diff > 1:
                return False
        return True