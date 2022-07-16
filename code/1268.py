class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        products.sort()
        for word_idx, word in enumerate(products):
            cur_trie = trie
            for letter in word:
                if letter not in cur_trie:
                    cur_trie[letter] = {}
                cur_trie = cur_trie[letter]
                # hash its word list to '$'
                if '$' in cur_trie:
                    cur_trie['$'].append(word_idx)
                else:
                    cur_trie['$'] = [word_idx]
        ans = []
        cur_trie = trie
        for letter in searchWord:
            if letter not in cur_trie:
                for _ in range(len(searchWord)-len(ans)):
                    ans.append([])
                break
            cur_trie = cur_trie[letter]
            sub_ans = cur_trie['$']
            sub_ans = sub_ans if len(sub_ans) <= 3 else sub_ans[:3]
            ans.append([products[num] for num in sub_ans])
        return ans