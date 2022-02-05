class Solution:
    def sumZero(self, n: int) -> List[int]:
        n_pair = n // 3 
        out_list = []
        for i in range(2,n_pair*2+2,2):
            out_list.append(i)
            out_list.append(i+1)
            out_list.append(-2*i-1)
        if n % 3 == 1:
            out_list.append(0)
        elif n % 3 == 2:
            out_list.append(-1)
            out_list.append(1)
        return out_list