from functools import lru_cache
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        @lru_cache(None)
        def explore(u, v):
            if u == v: return True
            return any(explore(child, v) for child in graph[u])

        return [explore(x, y) for x, y in queries]
