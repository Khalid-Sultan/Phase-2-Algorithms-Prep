# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
import math
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        mi = n
        while l<r:
            m = math.floor(l + (r-l)/2)
            if isBadVersion(m):
                r = m
                mi = min(mi, r) 
            else:
                l = m+1
        return mi