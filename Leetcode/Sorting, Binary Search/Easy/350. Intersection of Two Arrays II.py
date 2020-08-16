class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        ret = []
        if len(nums1)<len(nums2):
            for i in nums2:
                if i not in dic:
                    dic[i] = 0
                dic[i] += 1
            for j in nums1:
                if j in dic and dic[j]>0:
                    dic[j]-=1
                    ret.append(j)
        else:
            for i in nums1:
                if i not in dic:
                    dic[i] = 0
                dic[i] += 1
            for j in nums2:
                if j in dic and dic[j]>0:
                    dic[j]-=1
                    ret.append(j)
        return ret    