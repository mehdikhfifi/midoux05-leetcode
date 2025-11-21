class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for j in range(n//2):
            for i in range(n):
                matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
       