class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(max_sum):
            total_sum = 0
            count = 1
            for i in nums:
                total_sum += i
                if total_sum>max_sum:
                    total_sum = i
                    count += 1
                    if count>m:
                        return False
            return True
        left = right = 0
        for i in nums:
            left = max(left, i)
            right += i
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid     
            else:
                left = mid + 1
        return left