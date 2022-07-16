class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return True if target[0] == 1 else False
        hq = [-t for t in target]
        hq.sort()
        while sum(hq) < -len(target):
            max_val = heapq.heappop(hq)
            if max_val > sum(hq):
                return False
            prev_val = max_val - sum(hq)*((-max_val) // (-sum(hq))) if sum(hq) != -1 else -1
            if prev_val == 0:
                return False
            heapq.heappush(hq, prev_val)
        return True if sum(hq) == -len(target) else False
        