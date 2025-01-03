# https://neetcode.io/problems/design-twitter-feed
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # user id -> [(recency, tweet id)]
        self.follows = defaultdict(set) # user id -> {followees}
        self.recency = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.recency, tweetId))
        self.recency += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            for recency, tweet in self.tweets[followee][-10:]:
                heapq.heappush(feed, (recency, tweet))
                if len(feed) > 10:
                    heapq.heappop(feed)
        return [tweet for _, tweet in heapq.nlargest(10, feed)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
