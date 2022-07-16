class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp
        # (i, j)
        # if same = (i-1,j-1) + 1
        # if not the same max of (i,j-1) and (i-1,j)
        # init 
        # (i,0) if text1[i] == text2[0]: 1 else 0
        len1 = len(text1)
        len2 = len(text2)
        ans = []
        for i in range(len1):
            ans.append([0 for t in range(len2)])
        has_present = False
        for i in range(len1):
            has_present = True if text1[i] == text2[0] else has_present
            ans[i][0] = 1 if has_present else 0
        has_present = False
        for i in range(len2):
            has_present = True if text1[0] == text2[i] else has_present
            ans[0][i] = 1 if has_present else 0
        for i in range(1,len1):
            for j in range(1,len2):
                ans[i][j] = ans[i-1][j-1] + 1 if text1[i] == text2[j] else max(ans[i][j-1],ans[i-1][j])
        print(ans)
        return ans[len1-1][len2-1]
        