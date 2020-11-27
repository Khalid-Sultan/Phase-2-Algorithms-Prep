class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]

    #     return self.recur(0, s, {})
    # def recur(self, start, s, memo):
    #     if start in memo:
    #         return memo[start]
    #     if start>=len(s):
    #         if start==len(s):
    #             return 1
    #         return 0
    #     if s[start]=='0':
    #         return 0
    #     next_seq = self.recur(start+1, s, memo)
    #     if start<len(s)-1 and int(s[start]+s[start+1])<27:
    #         next_seq += self.recur(start+2, s, memo)
    #     memo[start] = next_seq
    #     return next_seq
