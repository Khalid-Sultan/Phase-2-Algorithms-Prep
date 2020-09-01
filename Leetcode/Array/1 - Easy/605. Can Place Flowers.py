class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0: return True
        for ind, i in enumerate(flowerbed):
            if i==0 and len(flowerbed)>2 and ind>0 and ind<len(flowerbed)-1 and flowerbed[ind-1]==0 and flowerbed[ind+1]==0:
                n-=1
                flowerbed[ind] = 1
            elif i==0 and ind==0 and flowerbed[ind+1]==0:
                n-=1
                flowerbed[ind] = 1
            elif i==0 and ind==len(flowerbed)-1 and flowerbed[ind-1]==0:
                n-=1
                flowerbed[ind] = 1
        return n<=0