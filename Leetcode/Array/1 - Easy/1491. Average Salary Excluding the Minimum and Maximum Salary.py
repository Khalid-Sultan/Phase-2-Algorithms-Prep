class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        max = 999
        min = 1000001
        len = -2
        for i in salary:
            sum += i
            len += 1
            if i<min:
                min = i
            if i>max:
                max = i
        return (sum - min - max)/len