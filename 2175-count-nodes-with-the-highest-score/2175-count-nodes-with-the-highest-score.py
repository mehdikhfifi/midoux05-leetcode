class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        graph = collections.defaultdict(list)
        n = len(parents)

        for child, parent in enumerate(parents):
            graph[parent].append(child)

        freq = collections.Counter()
        def count_nodes(node):
            # returns size of node tree, updates freq with its score
            p,s = 1,0
            for child in graph[node]:
                count_child = count_nodes(child)
                s += count_child
                p *= count_child
            p *= max(1, (n-1-s)) # everything above the node
            freq[p] +=1
            return s + 1


        count_nodes(0)
        return freq[max(freq.keys())] 


        



        