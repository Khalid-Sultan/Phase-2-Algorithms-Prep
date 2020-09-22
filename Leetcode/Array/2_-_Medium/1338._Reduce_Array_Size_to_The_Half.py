class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if not d.get(i):
                d[i] = 0
            d[i] += 1
        heap = []
        for key,value in d.items():
            heapq.heappush(heap, (-value, key))
        ct = len(arr)/2 if len(arr)%2==0 else (len(arr)+1)/2
        a = 0
        while ct>0:
            x = heappop(heap)
            ct-= -1 * x[0]
            a +=1
        return a
        