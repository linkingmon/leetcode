class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        hq = []
        time = 0
        for duration, lastday in sorted(courses, key=lambda x: x[1]):
            # traverse by its lastday
            time += duration # assume the task is taken
            heapq.heappush(hq, -duration)
            if time > lastday: # this task can not be scheduled, remove the longest duration
                remove_time = heapq.heappop(hq)
                time += remove_time
        return len(hq)
        