class Solution:
    def checkValidString(self, s: str) -> bool:
        def check(s, i, n_buf: List[int]):
            # print(i,n_buf)
            if i == len(s):
                return True if 0 in n_buf else False
            plus_buf = [t+1 for t in n_buf]
            minus_buf = []
            for t in n_buf:
                if t >= 1:
                    minus_buf.append(t-1)
            if s[i] == '(':
                n_buf = plus_buf
            elif s[i] == ')':
                n_buf = minus_buf
            else:
                n_buf = minus_buf + n_buf + plus_buf
                n_buf = list(set(n_buf))
            return check(s, i+1, n_buf)
        return check(s, 0, [0])
                