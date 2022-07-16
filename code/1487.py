class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        my_map = {};
        out_list = [];
        for name in names:
            if name in my_map:
                new_name = name + '(' + str(my_map[name]) + ')'
                while new_name in my_map: # Amortize
                    my_map[name] += 1
                    new_name = name + '(' + str(my_map[name]) + ')'
                my_map[new_name] = 1
                out_list.append(new_name)
            else:
                my_map[name] = 1
                out_list.append(name)
        return out_list