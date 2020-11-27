class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        common_ones = counter.most_common()
        frequency = common_ones[0][1]

        parts_count = frequency - 1
        parts_length = n - len(common_ones) - 1
        empty_slots = parts_count * parts_length
        available_tasks =   -(frequency*len(common_ones)) + len(tasks)
        idles = empty_slots - available_tasks
        return len(tasks) + max(0, idles)