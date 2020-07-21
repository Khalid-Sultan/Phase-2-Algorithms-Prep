class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = self.sort(heights)
        ret = 0
        for i in range(len(new_heights)):
            if heights[i]!=new_heights[i]:
                ret += 1
        return ret
    def sort(self,heights: List[int])->List[int]:
        nums = [0] * 101
        for i in heights:
            nums[i-1] += 1
        counter = 0
        ls = [0] * len(heights)
        for i in range(len(nums)):
            while nums[i]>0:
                ls[counter] = i+1
                counter+=1
                nums[i]-=1
        return ls
