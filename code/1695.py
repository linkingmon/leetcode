class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # do prefix sum
        prefix_sum = []
        sum_val = 0
        for i in range(len(nums)):
            sum_val += nums[i]
            prefix_sum.append(sum_val)
        prefix_sum.append(0)
        # sliding window with hash
        hash_num = {}
        cur_head = 0
        max_val = 0
        for i in range(len(nums)):
            if nums[i] in hash_num:
                prev_same_chr = hash_num[nums[i]]
                if prev_same_chr >= cur_head:
                    # prev_same_chr + 1 ~ i
                    max_val = max(max_val,prefix_sum[i]-prefix_sum[prev_same_chr])
                    cur_head = prev_same_chr + 1
                else:
                    # cur_head ~ i
                    max_val = max(max_val,prefix_sum[i]-prefix_sum[cur_head-1])
                hash_num[nums[i]] = i
            else:
                # cur_head ~ i
                hash_num[nums[i]] = i
                max_val = max(max_val,prefix_sum[i]-prefix_sum[cur_head-1])
            # print(i,hash_num,cur_head,max_val)
        return max_val
                