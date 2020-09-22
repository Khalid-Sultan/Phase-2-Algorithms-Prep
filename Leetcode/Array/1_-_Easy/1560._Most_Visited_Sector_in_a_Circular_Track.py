class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        round = [0]*101
        mx = 0
        for i in range(len(rounds)-1):
            if rounds[i+1]<=rounds[i]:
                for j in range(rounds[i], n+1):
                    round[j]+=1
                    mx = max(mx, round[j])
                for j in range(1,rounds[i+1]):
                    round[j]+=1
                    mx = max(mx, round[j])
            else:
                for j in range(rounds[i], rounds[i+1]):
                    round[j]+=1
                    mx = max(mx, round[j])
        round[rounds[i+1]]+=1
        mx = max(mx, round[rounds[i+1]])
        print(i,round)
        ret = []
        for ind,i in enumerate(round):
            if i==mx:
                ret.append(ind)
        return ret