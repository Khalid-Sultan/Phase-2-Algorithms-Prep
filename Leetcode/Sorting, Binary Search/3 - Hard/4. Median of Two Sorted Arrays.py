class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Solution 1
        return self.binary(nums1, nums2)

        #Solution 2
        # i = j = 0
        # ret = [0] * (len(nums1) + len(nums2))
        # ctr = 0
        # while i<len(nums1) and j<len(nums2):
        #     if nums1[i]<nums2[j]:
        #         ret[ctr] = nums1[i]
        #         ctr += 1
        #         i += 1
        #     elif nums1[i]>nums2[j]:
        #         ret[ctr] = nums2[j]
        #         ctr += 1
        #         j += 1
        #     else:
        #         ret[ctr] = nums1[i]
        #         ctr += 1
        #         ret[ctr] = nums2[j]
        #         ctr += 1
        #         i += 1
        #         j += 1
        # while i<len(nums1):
        #     ret[ctr] = nums1[i]
        #     ctr += 1
        #     i += 1
        # while j<len(nums2):
        #     ret[ctr] = nums2[j]
        #     ctr += 1
        #     j += 1
        # return self.getMedian(ret, len(ret))
    def getMedian(self, nums, length) -> float:
        print(nums)
        if length<=1:
            return 0 if length==0 else nums[0]
        return (nums[length//2]+nums[(length//2)-1]) / 2 if length%2==0 else nums[length//2]

    def binary(self, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        if l1<l2: return self.binary(nums2, nums1)
        l,r = 0, l2*2
        while l<=r:
            m2 = l + (r-l)//2
            m1 = l1 + l2 - m2
            
            A1 = -1 * (pow(2,32)-1) if m1==0 else nums1[(m1-1)//2]
            A2 = -1 * (pow(2,32)-1) if m2==0 else nums2[(m2-1)//2]
            B1 = pow(2,32)-1 if m1==l1*2 else nums1[(m1)//2]
            B2 = pow(2,32)-1 if m2==l2*2 else nums2[(m2)//2]
            
            if A1>B2:
                l = m2 + 1
            elif A2>B1:
                r = m2 - 1
            else:
                return (max(A1,A2) + min(B1, B2))/2

    
