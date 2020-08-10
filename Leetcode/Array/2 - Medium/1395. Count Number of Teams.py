class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # count = 0
        # for i in range(0,len(rating)-2,1):
        #     for j in range(i+1, len(rating)-1):
        #         for k in range(j+1, len(rating)):
        #             if rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]:
        #                 count+=1
        # return count
        c = 0
        for i,v in enumerate(rating[1:-1]):
            llc = rgc = lgc = rlc = 0
            for l in rating[:i+1]:
                if l < v:
                    llc += 1
                elif l > v:
                    lgc += 1
            for r in rating[i+2:]:
                if r > v:
                    rgc += 1
                elif r < v:
                    rlc += 1
            c += llc * rgc + lgc * rlc           
        return c