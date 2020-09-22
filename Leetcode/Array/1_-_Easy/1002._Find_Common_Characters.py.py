class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        s = [0] * 26
        for i in A[0]:
            s[ord(i)-97] += 1
        for i in range(1, len(A)):
            temp = [0]*26
            for c in A[i]:
                temp[ord(c)-97]+=1
            for d in range(26):
                s[d] = min(s[d], temp[d])
        ret = [] 
        for ind, i in enumerate(s):
            while i>0:
                ret.append(chr(ind+97))
                i-=1
        return ret