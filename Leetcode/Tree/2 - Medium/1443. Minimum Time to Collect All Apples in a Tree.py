class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        parents = {}
        apples = []
        count = 0
        for i in edges:
            if i[1] in parents:
                i = [i[1],i[0]]
            parents[i[1]] = i[0]
            if hasApple[i[1]]:
                parent = parents[i[1]]
                while parent!=0:
                    parent = parents[parent]
                apples.append(i[1])
        visited = set()
        for i in apples:
            ct = 0
            visited.add(i)
            parent = parents[i] if i in parents else -1
            while parent!=-1:
                if parent in visited:
                    if ct==0: 
                        ct = 1
                    else:
                        ct += 1
                    break
                ct+=1
                visited.add(parent)
                parent = parents[parent] if parent in parents else -1
            count+=ct*2
        return count 