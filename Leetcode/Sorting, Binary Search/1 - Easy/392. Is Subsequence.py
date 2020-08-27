class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev = 0
        
        for letter in s:
            found = False
            for i in range(prev, len(t)):
                if letter == t[i]:
                    prev = i+1
                    found = True
                    break
            if not found:
                return False
        return True