class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(list)
        self.postRec = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        postId = 1 + self.postRec
        self.posts[userId].append([-postId, tweetId])
        self.postRec += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        allPosts = []
        allPosts.extend(self.posts[userId])

        for followingId in self.following[userId]:
            allPosts.extend(self.posts[followingId])
        
        heapq.heapify(allPosts)
        for _ in range(10):

            if not allPosts:
                return res
            
            post = heapq.heappop(allPosts)
            res.append(post[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId or not followeeId or followerId == followeeId:
            return
        
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
