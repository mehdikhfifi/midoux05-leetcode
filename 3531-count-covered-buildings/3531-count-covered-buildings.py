class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        hashmap_y = collections.defaultdict(lambda: [100000, -1000000])
        hashmap_x = collections.defaultdict(lambda: [100000, -1000000])

        for x, y in buildings:
            hashmap_y[y][1] = max(hashmap_y[y][1], x)
            hashmap_y[y][0] = min(hashmap_y[y][0], x)

            hashmap_x[x][1] = max(hashmap_x[x][1], y)
            hashmap_x[x][0] = min(hashmap_x[x][0], y)
        res = 0
        print(hashmap_x)
        print(hashmap_y)
        for x, y in buildings:

            if (hashmap_x[x][0] < y and hashmap_x[x][1] > y) and (
                hashmap_y[y][0] < x and hashmap_y[y][1] > x
            ):
                res += 1
        return res
