class Solution:
    
    def commonFactors(self, a: int, b: int) -> int:
        c=[]
        for i in range(1,10001):
            if a%i==0 and b%i ==0:
                    c.append(i)
        return len(c)        


        