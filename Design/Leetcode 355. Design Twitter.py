class Tweet:
    ts = 0
    def __init__(self, tweetId):
        self.tweetId = tweetId
        self.ts = Tweet.ts
        Tweet.ts += 1
        
        
class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = []
        self.followeeIds = set()
        self.followeeIds.add(userId)
        
    def follow(self, followeeId):
        self.followeeIds.add(followeeId)
        
    def unfollow(self, followeeId):
        if followeeId in self.followeeIds:
            self.followeeIds.remove(followeeId)
    def post(self, tweetId):
        tweet = Tweet(tweetId)
        self.tweets.append(tweet)
        
import heapq        
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []
        if userId not in self.users:
            self.users[userId] = User(userId)
        followeeIds = self.users[userId].followeeIds
        for fid in followeeIds:
            user = self.users[fid]
            tweets.extend(user.tweets)
        heap = []
        for tweet in tweets:
            heapq.heappush(heap, (-tweet.ts, tweet.tweetId))
        newsFeed = []
        n = 10
        while heap and n>0:
            ts, tid = heapq.heappop(heap)
            newsFeed.append(tid)
            n -= 1
        return newsFeed
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
            
        self.users[followerId].follow(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
            
        self.users[followerId].unfollow(followeeId)