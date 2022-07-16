class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_zero(s):
            sum_val = 0
            for c in s:
                if c == '0':
                    sum_val += 1
            return sum_val
        n_zeros = [count_zero(string) for string in strs]
        n_ones = [len(strs[i])-n_zeros[i] for i in range(len(strs))]
        
        l = len(strs)
        ans_ary = [] # l x (m+1) x (n+1)
        for _ in range(l):
            sub_ans_ary = []
            for _ in range(m+1):
                sub_ans_ary.append([0]*(n+1))
            ans_ary.append(sub_ans_ary)
        # i_l = 0
        for i_m in range(m+1):
            for i_n in range(n+1):
                ans_ary[0][i_m][i_n] = 1 if (n_zeros[0] <= i_m and n_ones[0] <= i_n) else 0
        
        for i_l in range(1,l):
            for i_m in range(m+1):
                for i_n in range(n+1):
                    ans1 = ans_ary[i_l-1][i_m][i_n]
                    ans2 = -inf
                    if i_m >= n_zeros[i_l] and i_n >= n_ones[i_l]:
                        ans2 = ans_ary[i_l-1][i_m-n_zeros[i_l]][i_n-n_ones[i_l]]+1
                    # print(i_l,i_m,i_n,ans1,ans2)
                    ans_ary[i_l][i_m][i_n] = max(ans1, ans2)
        # print(ans_ary)
        return ans_ary[len(strs)-1][m][n]