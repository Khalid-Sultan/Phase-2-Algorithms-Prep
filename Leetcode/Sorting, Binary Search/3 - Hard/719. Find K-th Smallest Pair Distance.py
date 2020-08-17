class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(dist, length):
            ct = slow = fast = 0
            while slow < length or fast < length:
                while fast < length and nums[fast] - nums[slow] <= dist:
                    fast += 1
                ct += fast - slow - 1
                slow += 1
            return ct >= k
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        length = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if check(m, length):
                r = m
            else:
                l = m + 1
        return l