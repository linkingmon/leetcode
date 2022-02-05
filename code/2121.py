class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index_list = {}
        for i in range(len(arr)):
            cur_val = arr[i]
            if cur_val not in index_list.keys():
                index_list[cur_val] = [i]
            else:
                index_list[cur_val].append(i)
        output_list = [-1]*len(arr)
        for key, sub_index_list in index_list.items():
            sum_val = sum(sub_index_list) - sub_index_list[0]*len(sub_index_list)
            output_list[sub_index_list[0]] = sum_val
            for i in range(1,len(sub_index_list)):
                d = sub_index_list[i] - sub_index_list[i-1]
                sum_val = sum_val + i*d - (len(sub_index_list)-i)*d
                output_list[sub_index_list[i]] = sum_val
        return output_list