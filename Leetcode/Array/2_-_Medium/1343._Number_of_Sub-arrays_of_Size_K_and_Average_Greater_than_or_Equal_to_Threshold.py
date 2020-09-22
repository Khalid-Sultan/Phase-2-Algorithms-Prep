class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[0: k - 1])
        left = 0
        right = k - 1
        target = k*threshold
        ans = 0
        while left < len(arr) - k + 1:
            s += arr[right]
            if s >= target:
                ans += 1

            s -= arr[left]
            right += 1
            left += 1
        return ans