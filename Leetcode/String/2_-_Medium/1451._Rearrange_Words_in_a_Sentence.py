from heapq import *
class Solution:
    def arrangeWords(self, text: str) -> str:
        h = []
        for ind,i in enumerate(text.split()):
            heappush(h, (len(i), ind, i))
        s = []
        check = False
        while h:
            word = heappop(h)[2]
            if not check:
                s.append(word[0].upper() + word[1:])
                check = not check
            else:
                s.append(word.lower())
        return " ".join(s)