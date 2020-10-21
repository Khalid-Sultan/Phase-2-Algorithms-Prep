class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[1], x[0]))
        l = [0] * len(people)
        for i in range(len(people)):
            temp = people[i][1]
            for j in range(i):
                if people[j][0] >= people[i][0]:
                    if temp:
                        temp -= 1
                    else:
                        people = self.reshuffle(people, j, i)
                        break
        return people

    def reshuffle(self, people, start, end):
        before = people[:start]
        jump = people[start:end]
        after = people[end + 1:]
        current = [people[end]]
        return list(before + current + jump + after)

