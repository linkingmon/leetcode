class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort word by len
        words.sort(key=lambda word: len(word))
        dp = {word: 1 for word in words}
        ans = 1
        
        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[prev_word]+1, dp[word])
                    ans = max(ans, dp[word])
        
        return ans