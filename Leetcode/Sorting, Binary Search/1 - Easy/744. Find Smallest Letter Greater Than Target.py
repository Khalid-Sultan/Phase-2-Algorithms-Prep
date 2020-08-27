class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l<r:
            m = l + (r-l)//2
            if (ord(letters[m])-97)%26>(ord(target)-97)%26:
                r = m
            else:
                l = m+1
        return letters[l%len(letters)]