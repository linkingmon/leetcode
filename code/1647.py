class Solution:
    def minDeletions(self, s: str) -> int:
        cnt_ary = [0 for t in range(26)]
        for c in s:
            cnt_ary[ord(c)-97] += 1
        cnt_ary.sort()
        cnt_ary.reverse()
        prev_val = len(s) + 1
        ans = 0
        for i in range(26):
            if cnt_ary[i] == 0:
                break
            if cnt_ary[i] >= prev_val:
                prev_val = prev_val - 1 if prev_val > 0 else 0
                ans += (cnt_ary[i] - prev_val)
            else:
                prev_val = cnt_ary[i]
        return ans