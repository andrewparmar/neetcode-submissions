class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {k:[] for k in range(numCourses)}

        for x, y in prerequisites:
            prereq[x].append(y)

        def dfs(course, seen):
            if course in seen:
                return False
            if not prereq[course]:
                return True

            seen.add(course)
            for crs in prereq[course]:
                if not dfs(crs, seen):
                    return False
            seen.remove(course)

            prereq[course] = []
            return True

        seen = set()
        count = 0
        for course, _ in prereq.items():
            if dfs(course, seen):
                count += 1

        return count >= numCourses
            