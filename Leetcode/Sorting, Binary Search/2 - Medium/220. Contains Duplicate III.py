class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        tup = [(ind, i) for ind, i in enumerate(nums)]
        tup.sort(key=lambda x: x[1])
        for i in range(len(tup)):
            for j in range(i+1, len(tup)):
                if abs(tup[i][1]-tup[j][1])>t:
                    break
                if abs(tup[i][0]-tup[j][0])<=k:
                    return True
        return False