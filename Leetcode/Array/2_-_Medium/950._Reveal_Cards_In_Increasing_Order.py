class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # l = [0]*1000000
        # for i in deck:
        #     l[i-1]+=1
        # c = 0
        # for ind,i in enumerate(l):
        #     if c>=len(deck):
        #         break
        #     if i==0:
        #         continue
        #     deck[c] = ind+1
        #     l[ind]=0
        #     c+=1
        deck.sort()
        L = list(range(len(deck)))
        ret = [None]*len(deck)
        for i in deck:
            ret[L[0]] = i
            L = L[1:]
            if L:
                L.append(L[0])
                L = L[1:]
        return ret