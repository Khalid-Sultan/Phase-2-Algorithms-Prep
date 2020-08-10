class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_1 = -1
        for idx, i in enumerate(nums):
            if i==1:
                if prev_1==-1:
                    prev_1 = idx
                    continue
                if idx-prev_1-1>=k:
                    prev_1 = idx
                    continue
                return False
        return True