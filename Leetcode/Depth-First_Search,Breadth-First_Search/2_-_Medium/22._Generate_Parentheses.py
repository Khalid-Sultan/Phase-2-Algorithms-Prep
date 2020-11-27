class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, '', res, 0, 0)
        return res

    def dfs(self, n, string, result, opening, closing):
        if opening < closing:
            return
        if n == 0:
            cs = ')' * ((2 * opening) - len(string))
            result.append(string + cs)
            return
        self.dfs(n - 1, string.concat('('), string + '(', result, opening + 1, closing)
        self.dfs(n, string + ')', result, opening, closing + 1)


