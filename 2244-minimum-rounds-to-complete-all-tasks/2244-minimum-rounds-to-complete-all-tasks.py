class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        rounds = 0
        for task in counter:
            if counter[task] < 2:
                return -1
            rounds += math.ceil(counter[task] / 3)
        return rounds