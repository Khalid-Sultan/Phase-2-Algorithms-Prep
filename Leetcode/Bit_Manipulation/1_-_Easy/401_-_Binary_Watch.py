class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # We can technically remove the next two lines to make
        # the code more concise and avoid the space complexity
        a = [(str(i),bin(i).count("1")) for i in range(12)]
        b = [("{0:0=2d}".format(i),bin(i).count("1")) for i in range(60)]
        res = deque()
        for i in a:
            for j in b:
                if i[1]+j[1]==num:
                    res.append(i[0]+":"+j[0])
        return res