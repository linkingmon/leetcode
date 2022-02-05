class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        times = 0
        while True:
            if target <= startValue:
                break
            if target % 2 == 1:
                target = target + 1
            else:
                target = target // 2
            times = times + 1
        return startValue - target + times