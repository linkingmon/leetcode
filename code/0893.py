class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        sig_set = set()
        for word in words:
            sig_set.add(''.join(sorted(word[::2])) + ''.join(sorted(word[1::2])))
        return len(sig_set)