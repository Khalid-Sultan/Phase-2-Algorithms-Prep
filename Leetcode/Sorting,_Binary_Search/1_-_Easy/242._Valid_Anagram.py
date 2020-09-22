class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            l[ord(s[i])-97]+=1
            l[ord(t[i])-97]-=1
        for i in l:
            if i!=0:
                return False
        return True