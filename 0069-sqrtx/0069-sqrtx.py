class Solution:
    def mySqrt(self, x: int) -> int:
        self.x=x
        if self.x >= 0 :
            self.c=math.sqrt(self.x)
            return math.floor(self.c)
        else :
            return 'false'