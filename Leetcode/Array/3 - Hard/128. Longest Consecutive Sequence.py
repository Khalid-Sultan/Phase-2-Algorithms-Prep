class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)
        seen = set()
        for num in num_set:
            if(num not in seen):
                length = 0
                stack = [num]
                while(len(stack)>0):
                    last = stack.pop()
                    seen.add(last)
                    length+=1
                    if(last+1 not in seen and last+1 in num_set):
                        stack.append(last+1)
                    if(last-1 not in seen and last-1 in num_set):
                        stack.append(last-1)
                longest_streak = max(longest_streak, length)
        return longest_streak