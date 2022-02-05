class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        k_dict = {}
        for i in range(len(knowledge)):
            k_dict[knowledge[i][0]] = knowledge[i][1]
        out_s = ""
        temp_s = ""
        store = False
        for i in range(len(s)):
            if s[i] == '(':
                store = True
            elif store == True:
                if s[i] == ')':
                    print(temp_s)
                    # value = k_dict.pop(temp_s, None)
                    value = k_dict.get(temp_s)
                    out_s += value if value != None else '?'
                    temp_s = ""
                    store = False
                else:
                    temp_s += s[i]
            else:
                out_s += s[i]
        return out_s
            