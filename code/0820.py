class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        ans = 0
        for word_idx, word in enumerate(words):
            cur_trie = trie
            word = word[::-1]
            for letter in word:
                if '$' in cur_trie:
                    ans -= cur_trie['$']
                    cur_trie.pop('$')
                if letter not in cur_trie:
                    cur_trie[letter] = {}
                cur_trie = cur_trie[letter]
            # hash its word length to '$'
            if len(cur_trie) == 0:
                cur_trie['$'] = (len(word) + 1)
                ans += (len(word) + 1)
        return ans