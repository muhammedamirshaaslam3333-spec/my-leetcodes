class Solution:
    def maxDepth(self, s: str) -> int:
        self.count = 0 
        self.max = 0
        for i in s:
            if i =="(":
                self.count+=1
                if self.max < self.count:
                    self.max=self.count
                else:
                    pass
            elif i ==")":
                self.count -=1
        return self.max 
        