class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ob ={
            ')':'(',
            '}':'{',
            ']':'['        
            }
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val!=ob[i]:
                    return False
        return len(stack)==0
         
        