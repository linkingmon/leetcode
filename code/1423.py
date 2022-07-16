class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        prefix = [0]
        cur_sum = 0
        for card in cardPoints[:k]:
            cur_sum += card
            prefix.append(cur_sum)
        cardPoints.reverse()
        suffix = [0]
        cur_sum = 0
        for card in cardPoints[:k]:
            cur_sum += card
            suffix.append(cur_sum)
        suffix.reverse()
        return max([sum(x) for x in zip(prefix,suffix)])