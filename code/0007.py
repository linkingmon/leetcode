class Solution:
    def reverse(self, x: int) -> int:
        is_positive = (x > 0)
        x = x if is_positive else -x
        x_reverse = 0
        while x > 0:
            x_reverse = 10 * x_reverse + (x % 10)
            x = x // 10
        ans = x_reverse if is_positive else -x_reverse
        return ans if -(2**31)-1 < ans < 2**31 else 0