class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            sub_ary = []
            for j in range(len(matrix)):
                sub_ary.append(matrix[j][i])
            ans.append(sub_ary)
        return ans