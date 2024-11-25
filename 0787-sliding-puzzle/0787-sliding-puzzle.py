from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        


        start = ''.join(str(nums) for row in board for nums in row)

        target = '123450'
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }



        queue = deque([(start, 0)])
        visited = set([start])


        while queue:

            state, moves = queue.popleft()
            if state == target:
                return moves

            
            zero_idx = state.index('0')
            
            for neighbor in neighbors[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
                new_state = ''.join(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves +1))
        
        return -1


            