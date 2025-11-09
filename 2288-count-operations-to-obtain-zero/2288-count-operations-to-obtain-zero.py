
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        counter = 0
        def helper():
            nonlocal counter, num1, num2
            if num1 >= num2:
                num1-=num2
            else:
                num2-=num1
            counter+=1
        while num1 !=0 and num2 !=0:
            print(num1)
            print(num2)
            helper()
        
        return counter

                