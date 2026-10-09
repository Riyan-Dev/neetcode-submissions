class Twitter:

    def __init__(self):
        self.posts = []
        self.following = defaultdict(set)
        self.postRec = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (self.postRec, userId, tweetId))
        self.postRec -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = self.posts.copy()
        res = []

        while temp and len(res) < 10:

            time, authorId, tweetId = heapq.heappop(temp)

            if authorId == userId or authorId in self.following[userId]:
                res.append(tweetId)
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId or not followeeId or followerId == followeeId:
            return
        
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
