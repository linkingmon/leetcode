class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = ['@', '#', '$']
        cnt = [1]
        cur_char = '$'
        for i in range(len(s)):
            stk.append(s[i])
            if (s[i] == cur_char):
                cnt[-1] += 1
            else:
                cnt.append(1)
            cur_char = s[i]
            if cnt[-1] == k:
                for _ in range(k):
                    stk.pop()
                cnt.pop()
                cur_char = stk[-1]
        return ''.join(stk[3:])