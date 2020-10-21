class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        #         mapper = {}
        #         for i in nums:
        #             if i not in mapper:
        #                 mapper[i] = 0
        #             mapper[i]+=1
        #         h = list(zip(mapper.keys(), mapper.values()))
        #         heapify(h)

        #         while h:
        #             temp = []
        #             for i in range(k):
        #                 if not h:
        #                     return False
        #                 key, count = heappop(h)
        #                 if temp and temp[-1][0]!=key-1:
        #                     return False
        #                 temp.append((key, count))
        #             for i in temp:
        #                 if i[1]-1>0:
        #                     heappush(h, (i[0], i[1]-1))
        #         return True

        mapper = collections.Counter(nums)
        for key in sorted(mapper):
            while mapper[key]:
                for key1 in range(key, key + k):
                    if not mapper[key1]:
                        return False
                    mapper[key1] -= 1
        return True