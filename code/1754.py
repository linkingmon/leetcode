class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr_1 = 0
        ptr_2 = 0
        merge = ""
        word1 += "@"
        word2 += "@"
        while True:
            if word1[ptr_1] == word2[ptr_2]:
                if ptr_1 == len(word1) - 1 and ptr_2 == len(word2) - 1:
                    break
                if word1[ptr_1:] > word2[ptr_2:]:
                    merge += word1[ptr_1]
                    ptr_1 += 1
                else:
                    merge += word2[ptr_2]
                    ptr_2 += 1
            else:
                if word1[ptr_1] > word2[ptr_2]:
                    merge += word1[ptr_1]
                    ptr_1 += 1
                else:
                    merge += word2[ptr_2]
                    ptr_2 += 1

        return merge