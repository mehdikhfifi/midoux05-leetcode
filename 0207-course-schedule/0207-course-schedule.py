from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # graph is acyclic
        graph = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        
        visited = [False] * numCourses
        recursionStack = [False] * numCourses
        def dfs(node):
            nonlocal visited, recursionStack, graph

            if recursionStack[node]:
                return True
            if visited[node]:
                return False
            
            visited[node] = True
            recursionStack[node] = True            
            
            for child in graph[node]:
                if dfs(child):
                    return True
            recursionStack[node] = False
            return False
        
        for node in range(numCourses):
            a = visited[node]
            b = dfs(node)
            print(a,b)
            if not a and b:
                return False
        return True

        
        