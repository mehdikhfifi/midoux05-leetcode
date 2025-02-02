class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # monotonic stack ?



        stack = []


        for digit in num:
            while k > 0  and stack and stack[-1] > digit: 
                stack.pop()
                k-=1
            
            stack.append(digit)
        
        stack = stack[:len(stack) - k]
        
        # Convert stack to string and remove leading zeros
        result = "".join(stack).lstrip("0")
        
        # If result is empty, return "0"
        return result if result else "0"