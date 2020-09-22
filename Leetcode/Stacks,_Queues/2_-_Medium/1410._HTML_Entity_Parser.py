class Solution:
    def entityParser(self, text: str) -> str:
        buffer = deque()
        ins = False
        d = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        for i in text:
            if i=='&':
                buffer.append(i)
                ins = True
            elif i==';':
                buffer[-1] += i
                if buffer[-1] in d:
                    buffer[-1] = d[buffer[-1]]
                ins = False
            else:
                if ins:
                    buffer[-1]+=i
                else:
                    buffer.append(i)
        return "".join(buffer)