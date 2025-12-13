class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        events.sort(key =  lambda x: (int(x[1]), x[0] == "MESSAGE" ))
        last_online = {}
        for i in range(numberOfUsers):
            last_online[i] = 0
        res = [0 for _ in range(numberOfUsers)]
        for event in events:
            timestamp = int(event[1])
            if event[0] == 'MESSAGE':
                if event[2] == 'HERE':
                    for key in last_online.keys():
                        print(last_online[key])
                        if last_online[key] <= timestamp:
                            res[key] +=1
                elif event[2] == 'ALL':
                    res = [res[i] +1 for i in range(len(res))]
                else:
                    ids = [int(x[2:]) for x in event[2].split()]

                    for user in ids:
                        res[user] +=1
            else:
                user = int(event[2])
                last_online[user] = timestamp + 60
            
        return res





        