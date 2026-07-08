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
            res = []
            for crs in prereq[course]:
                res.append(dfs(crs, seen))
            seen.remove(course)

            return all(res)

        seen = set()
        count = 0
        for course, _ in prereq.items():
            if dfs(course, seen):
                count += 1

        return count >= numCourses
            