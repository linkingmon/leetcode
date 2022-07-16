class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word_idx, word in enumerate(words):
            concat_word = word + '#' + word # suffix + '#' + prefix
            for idx in range(len(word)):
                cur_trie = self.trie
                for letter in concat_word[idx:]:
                    if letter not in cur_trie:
                        cur_trie[letter] = {}
                    cur_trie = cur_trie[letter]
                    cur_trie['$'] = word_idx # hash its word_idx to '$'

    def f(self, prefix: str, suffix: str) -> int:
        concat_word = suffix + '#' + prefix
        cur_trie = self.trie
        for letter in concat_word:
            if letter not in cur_trie:
                return -1
            cur_trie = cur_trie[letter]
        return cur_trie['$']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)