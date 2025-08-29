class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [False] * numCourses
        recursionStack = [False] * numCourses
        ordering = []
        def dfs(node):
            nonlocal visited, recursionStack, graph
            if recursionStack[node]: 
                """ 
                recursion stack condition must be first
                imagine ur exploring node A and mark it as true in both visited and recursion stack
                when u reach a child that has a back-edge, itif it checks visited[node] = false first it
                will return false and will skip the actual cycle detection step
                """
                return True
            if visited[node]:
                return False
            visited[node] = True
            recursionStack[node] = True
            for child in graph[node]:
                if dfs(child):
                    return True
            recursionStack[node] = False
            ordering.append(node)
            return False
            
            
        for node in range(numCourses):
            if not visited[node] and  dfs(node):
                return []
        return ordering[::-1] # reverse post order
