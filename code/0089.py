class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        l = self.grayCode(n-1)
        l_r = l.copy()
        l_r.reverse()
        add = 2**(n-1)
        return l + [t+add for t in l_r]