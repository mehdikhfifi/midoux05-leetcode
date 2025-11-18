class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        first = 0
        second  = 1
        while first < len(bits) or second < len(bits):
            if bits[first] == 0:
                if (first == len(bits)-1):
                    return True
                first +=1
                second +=1
            elif  (bits[first], bits[second])== (1,1) or  (bits[first], bits[second])== (1,0):
                first += 2
                second += 2
            else:
                return True
        return False


            

        