class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        


        graph = defaultdict(list)
        indeg = [0] * numCourses
        for prereq, course in prerequisites:
            graph[prereq].append(course)
            indeg[course] +=1
        
        prereq_sets = [set() for _ in range(numCourses)]
        q = deque([i for i in range(numCourses) if indeg[i] ==0])

        while q:
            u = q.popleft()
            for v in graph[u]:
                prereq_sets[v].add(u)
                prereq_sets[v] |= prereq_sets[u] # adding all prereqs of u as they are obvs prereqs of v as well
                indeg[v] -=1
                if indeg[v] ==0:
                    q.append(v)
        
        return [(x in prereq_sets[y]) for x,y in queries]
        
        

