class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        #Find Largest Number
        #Rotate to make largest at the first
        #Rotate to make largest at the last position
        #Do it again till the min is at first        
        min, max = 0, 0
        for i in range(len(A)):
            if A[i]<A[min]:
                min = i
            if A[i]>A[max]:
                max = i
        
        ret = []
        if max != len(A)-1:            
            A = A[:max+1][::-1] + A[max+1:]
            A = A[::-1]
            ret = [max+1, len(A)]
        end = len(A)-1
        while min != 0 or end>=0:
            min, max = 0, 0
            for i in range(end):
                if A[i]<A[min]:
                    min = i
                if A[i]>A[max]:
                    max = i
            if max != end:       
                A = A[:max+1][::-1] + A[max+1:]
                A = A[:end][::-1] + A[end:]
                ret += [max+1, end]
            end-=1                    
        return ret
