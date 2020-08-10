class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        uno = 0
        dos = 0
        for i in nums:
            if i>uno:
                temp = uno
                uno = i
                if temp>dos:
                    dos = temp
            elif i==uno:
                if i>dos:
                    dos = i
            elif i>dos:
                dos = i
        return (uno-1) * (dos-1)