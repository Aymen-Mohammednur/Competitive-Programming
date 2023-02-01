class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        dp = [players[i][0] for i in range(len(players))]
        for i in range(len(players)):
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], players[i][0] + dp[j])
        return max(dp)