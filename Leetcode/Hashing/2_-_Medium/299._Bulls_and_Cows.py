class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = set()
        bulls = cows = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                s.add(i)
        count = [0 for i in range(10)]
        for ind, i in enumerate(secret):
            if ind not in s:
                count[int(i)]+=1
        print(count)
        for ind, i in enumerate(guess):
            if ind not in s and count[int(i)]>0:
                cows+=1
                count[int(i)]-=1
        return str(bulls)+"A"+str(cows)+"B"