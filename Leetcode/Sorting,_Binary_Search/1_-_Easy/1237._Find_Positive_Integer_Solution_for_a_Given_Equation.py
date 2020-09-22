"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # ls = []
        # for i in range(1,z+1):
        #     for j in range(1,z+1):
        #         if customfunction.f(i,j)==z:
        #             ls.append([i,j])
        # return ls
        rst = []
        l, r = 1, z
        while l <= z and r > 0:
            cur = customfunction.f(l, r)
            if cur < z: l += 1
            elif cur > z: r -= 1
            else: 
                rst.append((l, r))
                l, r = l+1, r-1
        return rst