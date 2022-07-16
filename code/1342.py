class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while (num != 0 and num != 1):
            if num & 1 == 1:
                ans += 2
            else:
                ans += 1
            num >>= 1
        return ans + num