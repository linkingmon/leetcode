class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_ary = deque()
        min_ary = deque()
        left_idx = 0
        max_deep = 0
        for i in range(0,len(nums)):
            while max_ary and nums[i] >= nums[max_ary[-1]]:
                max_ary.pop()
            while min_ary and nums[i] <= nums[min_ary[-1]]:
                min_ary.pop()
            max_ary.append(i)
            min_ary.append(i)
            if nums[max_ary[0]] - nums[min_ary[0]] > limit:
                if left_idx == max_ary[0]:
                    max_ary.popleft()
                if left_idx == min_ary[0]:
                    min_ary.popleft()
                left_idx = left_idx + 1
            max_deep = max(max_deep,i - left_idx + 1)
        return max_deep