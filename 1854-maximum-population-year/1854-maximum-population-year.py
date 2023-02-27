class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
        dates.sort()
        population, max_population, res = 0, 0, 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                res = year
        return res