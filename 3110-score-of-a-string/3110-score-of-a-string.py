class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0 
        le = 0 
        for i in range(len(s)-1):
            sum = ord(s[i]) - ord(s[i+1])
            
            le+=abs(sum)
        return le
        
            
        