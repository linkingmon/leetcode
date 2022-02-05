class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]
        for i in range(len(s)):
            is_palindrome = True
            for j in range(len(s)):
                if i-j < 0 or i+j >= len(s):
                    break
                if s[i-j] != s[i+j]:
                    is_palindrome = False
                    break
                if 2*j+1 > max_len:
                    max_len = 2*j+1
                    max_str = s[i-j:i+j+1]
            if (i+1 < len(s)) and (s[i] == s[i+1]):
                is_palindrome = True
                if 2 > max_len:
                    max_len = 2
                    max_str = s[i:i+2]
            else:
                continue
            for j in range(len(s)-1):
                if i-j < 0 or i+j+1 >= len(s):
                    break
                if s[i-j] != s[i+j+1]:
                    is_palindrome = False
                    break
                if 2*j+2 > max_len:
                    max_len = 2*j+2
                    max_str = s[i-j:i+j+2]
        return max_str
