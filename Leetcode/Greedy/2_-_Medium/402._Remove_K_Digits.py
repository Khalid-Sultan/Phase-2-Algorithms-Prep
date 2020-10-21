class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        z = k
        if k==0: return num
        if len(num)==k: return "0"
        if len(num)==2: return "0" if k==2 else str(min(int(num[0]),int(num[1])))
        stack = deque()
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        while stack and k>0:
            stack.pop()
            k-=1
        res = ""
        while stack:
            res += stack.popleft()
        return str(int(res))