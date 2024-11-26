from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return -1  # No teams present

        # Initialize in-degree for all teams to 0
        in_degree = [0] * n

        # Compute in-degree for each team
        for u, v in edges:
            in_degree[v] += 1

        # Identify all teams with zero in-degree
        champions = [i for i in range(n) if in_degree[i] == 0]

        # Determine if there's a unique champion
        if len(champions) == 1:
            return champions[0]
        else:
            return -1
