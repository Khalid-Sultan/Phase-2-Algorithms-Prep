from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        buffer = deque()
        start = True
        l = ""
        for i in range(1, len(path)):
            if path[i]=='/':
                l+='/'
                if l=="../":
                    if buffer: 
                        buffer.pop()
                elif l=="./" or l=="/":
                    l = ""
                elif l!="":
                    buffer.append(l)
                
                l = ""
            else:
                l+=path[i]
        if l=="..":
            if buffer:
                buffer.pop()
        elif l!="." and l!="":
            buffer.append(l)
        if buffer and buffer[-1][-1]=='/':
            s = buffer.pop()
            buffer.append(s[:-1])
        return "/" + "".join(buffer)
                
