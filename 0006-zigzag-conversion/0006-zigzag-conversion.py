class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows = [""for _ in range(numRows)]
        level = 0

        order = [_ for _ in range(numRows)] + [_ for _ in range(numRows-2, 0, -1)]

        for index, char in enumerate(s):
            rows[order[level]] += char
            level = (level + 1) % len(order)
        
        res = ""
        print(rows)
        for fragment in rows:
            res += fragment
    
        return res


        