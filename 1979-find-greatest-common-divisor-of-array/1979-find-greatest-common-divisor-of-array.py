class Solution:
    def findGCD(self, nums: List[int]) -> int:
        c=[]
        for i in range(1,1001):
            if min(nums)%i==0 and max(nums)%i==0:
                c.append(i)
               
                
            else :
                pass
        return max(c)

        