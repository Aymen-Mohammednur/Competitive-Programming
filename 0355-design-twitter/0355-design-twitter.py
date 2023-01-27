class Twitter:

    def __init__(self):
        self.user_followers = defaultdict(set)
        self.user_tweets = defaultdict(set)
        self.all_tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].add(tweetId)
        self.all_tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 0
        for i in range(len(self.all_tweets) - 1, -1, -1):
            user, tweet = self.all_tweets[i]
            if user in self.user_followers[userId] or user == userId:
                res.append(tweet)
                count += 1
            if count == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)