class Twitter:

    def __init__(self):
        self.tweet = {}
        self.time = 0
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweet:
            self.tweet[userId] = []
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        if userId in self.tweet:
            feed.extend(self.tweet[userId])

        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.tweet:
                    feed.extend(self.tweet[followee])

        feed.sort(reverse=True)
        ans = []

        for time, tweetId in feed[:10]:
            ans.append(tweetId)

        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId)
