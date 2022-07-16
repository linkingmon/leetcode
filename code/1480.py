class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for idx, num in enumerate(nums):
            if idx == 0:
                ans.append(num)
            else:
                ans.append(ans[-1]+num)
        return ans