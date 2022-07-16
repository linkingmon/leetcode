class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_char = [-1 for t in range(256)]
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            prev_idx = hash_char[ord(s[i])]
            cur_len = cur_len + 1 if (i - prev_idx) > cur_len else i - prev_idx
            max_len = max(max_len, cur_len)
            hash_char[ord(s[i])] = i
        return max_len