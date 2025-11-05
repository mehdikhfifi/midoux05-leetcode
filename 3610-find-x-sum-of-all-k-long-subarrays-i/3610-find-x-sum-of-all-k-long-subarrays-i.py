class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        

        res = []

        for i in range(len(nums)-k+1):

            temp = []
            mymap = defaultdict(int)
            j = i
            while j < i + k:
                temp.append(nums[j])
                mymap[nums[j]] += 1
                j+=1

            temp.sort(key = lambda x: (mymap[x], x), reverse = True)
            print(temp)
            seen = set()
            temp = [elem for elem in temp if (elem in seen or (len(seen) <x and not seen.add(elem)))]
            print(temp)
            res += [sum(temp)]
        
        return res