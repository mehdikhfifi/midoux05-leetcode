class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        appendone = False
        for index, x in enumerate(reversed(digits)):
            if x != 9:
                digits[n-1-index] +=1
                break
            elif index == len(digits)-1:
                appendone = True
            digits[n-1-index] = 0
        if appendone:
            digits.insert(0,1)
        return digits


        