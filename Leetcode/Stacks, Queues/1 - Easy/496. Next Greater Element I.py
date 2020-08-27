from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # for i in range(len(nums1)):
        #     r = -1
        #     for j in range(nums2.index(nums1[i]), len(nums2)):
        #         if nums1[i]<nums2[j]:
        #             r = nums2[j]
        #             break
        #     nums1[i] = r
        # return nums1
        positions = {}
        buffer = deque()
        
        for x in nums2:
            while len(buffer) and buffer[-1] < x:
                positions[buffer.pop()] = x
            buffer.append(x)

        result = [positions.get(i, -1) for i in nums1]
        return result

        