class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B) or len(A)<2 or len(B)<2: return False
        rem = []
        ct = [0]*26
        for i in range(len(A)):
            if A[i]!=B[i]:
                rem.append(i)
                if len(rem)>2: return False
            ct[ord(A[i])-97]+=1
        if len(rem)==2: 
            t = [i for i in A]
            print(rem)
            t[rem[0]], t[rem[1]] = t[rem[1]], t[rem[0]]
            A = "".join(t)
            return A==B
        if A!=B: return False
        for i in ct:
            if i>=2: return True
        return False