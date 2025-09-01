class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        


        myboard = [[False] * len(board[0]) for _ in range(len(board)) ]
        counter = 0
        m = len(board)
        n = len(board[0])

        def explore(i,j):
            differential = [(0,1), (1,0), (0,-1), (-1,0)]
            # set the board to true first
            for diff in differential:
                x,y = (i,j)
                while ((0 <= x < m and 0<= y <n) and board[x][y] == 'X'):
                    myboard[x][y] = True
                    x += diff[0]
                    y += diff[1]

            
        for i in range(m):
            for j in range(n):
                if myboard[i][j]:
                    continue
                elif board[i][j] == 'X':
                    explore(i,j)
                    counter +=1
                else:
                    myboard[i][j] = True




        return counter