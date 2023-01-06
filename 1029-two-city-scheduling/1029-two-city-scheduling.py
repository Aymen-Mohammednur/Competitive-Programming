class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        from_a_to_b = []
        cost = 0
        for a, b in costs:
            cost += a
            from_a_to_b.append(b - a)
        from_a_to_b.sort()
        for i in range(len(costs) // 2):
            cost += from_a_to_b[i]
        return cost