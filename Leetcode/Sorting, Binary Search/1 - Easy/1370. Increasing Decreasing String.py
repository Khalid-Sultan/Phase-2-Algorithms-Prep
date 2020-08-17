class Solution:
    def sortString(self, s: str) -> str:
        l = []
        c = [0] * 26
        asc = True
        for i in s:
            c[ord(i)-97]+=1
        while len(l)<len(s):
            for i in range(26):
                i = i if asc else 25-i
                if c[i]>0:
                    l.append(chr(i+97))
                    c[i]-=1
            asc = not asc    
        return ''.join(l)
                    