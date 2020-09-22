class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = set(nums1)
        ret = [i for i in nums2 if i in l]
        return list(set(ret))