class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        l = [0]*26
        for i in s:
            index = ord(i)-ord('a')
            l[index]+=1

        for i in t:
            indes = ord(i)-ord('a')
            l[indes]-=1
            if(l[indes]<0):
                return False
        return True