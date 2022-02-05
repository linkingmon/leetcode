class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        longest = 0 # longest length in [:i]
        TF_count = {'T': 0, 'F': 0} # max 'T' or 'F' in longest
        for i in range(len(answerKey)):
            TF_count[answerKey[i]] += 1
            # if i become longest, it is the substring with length longest+1 end at i
            if longest + 1 - max(TF_count['T'],TF_count['F']) <= k:
                longest += 1
            else:
                TF_count[answerKey[i-longest]] -= 1
        return longest