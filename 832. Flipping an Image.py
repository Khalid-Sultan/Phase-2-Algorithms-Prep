class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:            
            mid_point = len(row)
            if mid_point%2!=0:
                mid_point = int((mid_point-1)/2)
                row[mid_point] = 1 if row[mid_point]==0 else 0
            else:
                mid_point = int(mid_point/2)
            for i in range(mid_point):
                temp = row[i]
                row[i] = 1 if row[len(row)-1-i]==0 else 0
                row[len(row)-1-i] = 1 if temp==0 else 0
        return A
        