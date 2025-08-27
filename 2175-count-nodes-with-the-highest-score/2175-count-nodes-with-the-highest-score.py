class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        

        graph = collections.defaultdict(list)
        n = len(parents)
        for child, parent in enumerate(parents):
            graph[parent].append(child)
        freq = Counter()
        def count_nodes(node):
            s,p = 0,1
            
            for child in graph[node]:
                res = count_nodes(child)
                s+= res
                p*= res
            p *= max(1, (n-1-s))
            freq[p] += 1
            return s +1



        count_nodes(0)
        return freq[max(freq.keys())]