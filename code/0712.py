class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1_len = len(s1)
        s2_len = len(s2)
        # ans[i][j] : answer of 0:i 0:j
        ans = [[[0] for _ in range(s2_len)] for _ in range(s1_len)]
        has_char = False
        sum_val = 0
        for i in range(s1_len):
            sum_val += ord(s1[i])
            has_char = True if s1[i] == s2[0] else has_char
            ans[i][0] = sum_val + ord(s2[0]) if has_char == False else sum_val - ord(s2[0])
        has_char = False
        sum_val = 0
        for j in range(s2_len):
            sum_val += ord(s2[j])
            has_char = True if s2[j] == s1[0] else has_char
            ans[0][j] = sum_val + ord(s1[0]) if has_char == False else sum_val - ord(s1[0])
        for i in range(1,s1_len):
            for j in range(1,s2_len):
                if s1[i] == s2[j]:
                    ans[i][j] = ans[i-1][j-1]
                else:
                    ans[i][j] = min(ans[i][j-1] + ord(s2[j]),ans[i-1][j] + ord(s1[i]))
        return ans[-1][-1]