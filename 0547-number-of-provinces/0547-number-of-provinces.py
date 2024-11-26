import numpy as np

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        
        return int(len(M) - np.linalg.matrix_rank(np.diag(np.sum(M, axis=1)) - np.array(M)))