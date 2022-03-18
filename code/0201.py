class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cur_demod = 2
        ans = 0
        while True:
            left_div = left // cur_demod
            right_div = right // cur_demod
            left_mod = left % cur_demod
            right_mod = right % cur_demod
            if left_div == right_div and (cur_demod >> 1) <= left_mod <= right_mod:
                ans += (cur_demod >> 1)
            if left_div == 0 and right_div == 0:
                break
            cur_demod = cur_demod << 1
        return ans