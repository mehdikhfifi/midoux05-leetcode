from collections import defaultdict

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        

        start = ''.join(str(num) for row in board for num in row)

        target = '123450'


        neighbours = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }

        queue = deque([(start, 0)]) 
        visited = set([start])

        while queue:
            current, moves = queue.popleft()


            if current == target:
                return moves
            zero_idx= current.index('0')

            for neighbor in neighbours[zero_idx]:
                new_state = list(current)
                new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
                new_state = ''.join(new_state)


                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves+1))
        
        return -1



