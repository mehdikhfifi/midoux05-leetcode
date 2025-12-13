import heapq

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        online = set(range(numberOfUsers))
        heap = []  # (reactivate_time, user)
        res = [0] * numberOfUsers

        for event in events:
            timestamp = int(event[1])

            # Reactivate users
            while heap and heap[0][0] <= timestamp:
                _, user = heapq.heappop(heap)
                online.add(user)

            if event[0] == "OFFLINE":
                user = int(event[2])
                online.remove(user)
                heapq.heappush(heap, (timestamp + 60, user))

            else:  # MESSAGE
                if event[2] == "ALL":
                    for i in range(numberOfUsers):
                        res[i] += 1

                elif event[2] == "HERE":
                    for user in online:
                        res[user] += 1

                else:
                    for token in event[2].split():
                        user = int(token[2:])
                        res[user] += 1

        return res
