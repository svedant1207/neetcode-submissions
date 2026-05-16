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

        for time, tweetId in self.tweet[userId]:
            heapq.heappush(feed, (-self.time, tweetId))

        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.tweet:
                    for time, tweetId in self.tweet[followee]:
                        heapq.heappush(feed, (-time, tweetId))
        ans = [] 
        for i in range(10):
            if feed:
                ans.append(heapq.heappop(feed)[1])
        return ans

        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)