class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        num = {}
        for i in range(len(answers)):
            if answers[i] not in num.keys():
                num[answers[i]] = 1
            else:
                num[answers[i]] += 1
        sum_value = 0
        for key, value in num.items():
            n_pair = value // (key + 1)
            remain = value % (key+1)
            sum_value = sum_value + (n_pair*(key+1))
            sum_value = sum_value+key+1 if remain != 0 else sum_value
        return sum_value