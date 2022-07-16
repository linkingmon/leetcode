class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        # sorted by decreasing height
        for h, k in people:
            result.insert(k, [h, k])
            # insert shorter value will not affect k
            # print(result)
        return result
        