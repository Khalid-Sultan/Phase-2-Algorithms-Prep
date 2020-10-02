class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ret = []
        # for ind, i in enumerate(favoriteCompanies):
        #     favoriteCompanies[ind] = set(sorted(i))
        for ind, current_person in enumerate(favoriteCompanies):
            check = False
            for j in range(len(favoriteCompanies)):
                if ind == j: continue
                previous_person = favoriteCompanies[j]
                if len(list(set(current_person) & set(previous_person))) == len(current_person):
                    check = True
                    break
            if not check:
                ret.append(ind)
        return ret
