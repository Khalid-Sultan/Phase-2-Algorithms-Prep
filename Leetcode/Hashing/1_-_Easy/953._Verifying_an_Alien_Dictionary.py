POS = None


class Solution:
    class MyStrOrder:
        def __init__(self, inner):
            self.inner = inner

        def __lt__(self, other):
            global POS
            for i in range(min(len(self.inner), len(other.inner))):
                a = POS.get(self.inner[i])
                b = POS.get(other.inner[i])
                if a != b:
                    return a < b
            return len(self.inner) < len(other.inner)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        global POS
        POS = {c: p for (p, c) in enumerate(order)}
        srt = sorted(words, key=self.MyStrOrder)
        for i in range(len(words)):
            if words[i] != srt[i]:
                return False
        return True