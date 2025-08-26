# Design Twitter

## Problem
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- `Twitter()` Initializes your twitter object
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID tweetId by the user userId
- `List<Integer> getNewsFeed(int userId)` Retrieves the 10 most recent tweet IDs in the user's news feed
- `void follow(int followerId, int followeeId)` The user with ID followerId started following the user with ID followeeId
- `void unfollow(int followerId, int followeeId)` The user with ID followerId unfollows followeeId

## My Approach

I use a k-way merge approach similar to merging k sorted lists. Each user's tweets are stored in chronological order with timestamps. When generating a news feed, I use a max heap to efficiently merge tweets from all followed users (including self) and return the 10 most recent.

## Solution with Comments

```python
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.clock = 0  # Global timestamp counter for ordering tweets
        self.network = defaultdict(dict)  # Store user data
        """
        Data structure design:
        {
            userId: {
                "tweets": [(timestamp, tweetId), ...],  # List of tweets in chronological order
                                                        # Stored as tuples for easy sorting
                                                        # Could use deque(maxlen=10) to limit memory
                "followings": set()  # Set for O(1) follow/unfollow operations
            }
        }
        Why this structure:
        - List for tweets: Maintains insertion order, allows index access for k-way merge
        - Set for followings: O(1) add/remove, no duplicates
        - Global clock: Ensures unique timestamps across all users
        """

    def _create_user(self, userId: int) -> None:
        """Helper to create user if doesn't exist"""
        if userId not in self.network:
            self.network[userId] = {
                "tweets": [],
                "followings": set()
            }

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment clock BEFORE using it to ensure each tweet has unique timestamp
        self.clock += 1  
        self._create_user(userId)  # Lazy user creation
        # Store as (timestamp, tweetId) tuple for easy sorting/comparison
        self.network[userId]["tweets"].append((self.clock, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        K-way merge algorithm to get 10 most recent tweets from followed users.
        Similar to merging k sorted lists where each user's tweets are a sorted list.
        """
        # Handle edge case: user doesn't exist (e.g., called right after initialization)
        # Create user lazily for consistency with other methods
        self._create_user(userId)
        
        tweets = []  # Max heap for k-way merge
        
        # Get all users whose tweets should appear in feed
        # Use copy() to avoid modifying original followings set
        feed_candidates = self.network[userId]["followings"].copy()
        feed_candidates.add(userId)  # User sees their own tweets too
        
        # Initialize heap with most recent tweet from each user
        # This is like taking the head of each sorted list in k-way merge
        for followeeId in feed_candidates:
            if followeeId in self.network and self.network[followeeId]["tweets"]:
                # Start from the end (most recent tweet)
                index = len(self.network[followeeId]["tweets"]) - 1
                time, tweetId = self.network[followeeId]["tweets"][index]
                
                # Heap tuple structure: (-time, tweetId, followeeId, index)
                # -time: Negative for max heap (Python only has min heap)
                # tweetId: The actual tweet to return
                # followeeId: Which user this tweet belongs to
                # index: Position in that user's tweet list for getting next tweet
                heapq.heappush(tweets, (-time, tweetId, followeeId, index))
        
        feed = []
        # K-way merge: extract 10 most recent tweets
        while tweets and len(feed) < 10:
            # Pop the most recent tweet across all users
            time, tweetId, followeeId, index = heapq.heappop(tweets)
            feed.append(tweetId)
            
            # Add next tweet from same user if exists
            # This maintains the "k streams" in our k-way merge
            if index > 0:  # Check if user has older tweets
                # Get previous tweet (index - 1 moves backward in time)
                time, tweetId = self.network[followeeId]["tweets"][index - 1]
                heapq.heappush(tweets, (-time, tweetId, followeeId, index - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent self-following which would duplicate tweets in feed
        if followerId != followeeId:  
            self._create_user(followerId)  # Create follower if doesn't exist
            # Set automatically handles duplicates, so safe to add
            self.network[followerId]["followings"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Check both user exists and is actually following to avoid KeyError
        if followerId in self.network and followeeId in self.network[followerId]["followings"]:
            self.network[followerId]["followings"].remove(followeeId)
        # Note: Could use discard() instead of remove() to avoid checking
```

## Optimized Solution with Memory Limit

```python
from collections import defaultdict, deque
import heapq

class Twitter:
    def __init__(self):
        self.clock = 0
        self.MAX_TWEETS_PER_USER = 10  # Only store recent tweets
        self.users = defaultdict(lambda: {"tweets": deque(maxlen=self.MAX_TWEETS_PER_USER), 
                                          "followings": set()})

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1
        # Deque automatically removes oldest when full
        self.users[userId]["tweets"].append((self.clock, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        # Include self and followings
        feed_sources = self.users[userId]["followings"] | {userId}
        
        # Add most recent tweet from each source
        for uid in feed_sources:
            if self.users[uid]["tweets"]:
                tweets_list = list(self.users[uid]["tweets"])
                index = len(tweets_list) - 1
                time, tid = tweets_list[index]
                heapq.heappush(max_heap, (-time, tid, uid, tweets_list, index))
        
        feed = []
        while max_heap and len(feed) < 10:
            time, tid, uid, tweets_list, index = heapq.heappop(max_heap)
            feed.append(tid)
            
            if index > 0:
                next_tweet = tweets_list[index - 1]
                heapq.heappush(max_heap, (-next_tweet[0], next_tweet[1], 
                                         uid, tweets_list, index - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId]["followings"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId]["followings"].discard(followeeId)
```

## Visual Intuition

### K-Way Merge Process

```
User1 tweets: [(5, "t5"), (3, "t3"), (1, "t1")]
User2 tweets: [(6, "t6"), (2, "t2")]
User3 tweets: [(4, "t4")]

Initial Max Heap (most recent from each):
    (-6, "t6", User2, idx=1)
   /                        \
(-5, "t5", User1, idx=2)    (-4, "t4", User3, idx=0)

Step 1: Pop (-6, "t6")
- Add "t6" to feed
- Push User2's next: (-2, "t2", User2, idx=0)

Step 2: Pop (-5, "t5")
- Add "t5" to feed
- Push User1's next: (-3, "t3", User1, idx=1)

Continue until 10 tweets or heap empty...
Final feed: ["t6", "t5", "t4", "t3", "t2", "t1"]
```

### Data Structure Visualization

```
network = {
    1: {
        "tweets": [(1, 101), (3, 103), (7, 107)],
        "followings": {2, 3}
    },
    2: {
        "tweets": [(2, 201), (5, 205)],
        "followings": {1}
    },
    3: {
        "tweets": [(4, 301), (6, 306), (8, 308)],
        "followings": set()
    }
}

Getting feed for User 1:
- Include: User 1 (self), User 2, User 3
- Merge their tweets by timestamp
- Result: [308, 107, 306, 205, 301, 103, 201, 101]
```

## Complexity Analysis

### postTweet
- **Time Complexity:** O(1)
  - Append to list is O(1)
  
### getNewsFeed
- **Time Complexity:** O(N log k)
  - k = number of followings + 1 (self)
  - N = 10 (maximum tweets to return)
  - Each heap operation is O(log k)
  
- **Space Complexity:** O(k)
  - Heap stores at most k elements

### follow/unfollow
- **Time Complexity:** O(1)
  - Set operations are O(1)

## Edge Cases

```python
# Edge Case 1: User follows themselves
# Should be prevented in follow()

# Edge Case 2: User unfollows someone they don't follow
# Should handle gracefully with discard()

# Edge Case 3: User with no tweets
# Should handle empty tweet lists

# Edge Case 4: User with no followings
# Should still see own tweets

# Edge Case 5: Less than 10 total tweets
# Return all available tweets

# Edge Case 6: User doesn't exist
# Create user on demand

# Edge Case 7: getNewsFeed called immediately after initialization
twitter = Twitter()
twitter.getNewsFeed(1)  # User 1 doesn't exist yet
# Fixed by: self._create_user(userId) at start of getNewsFeed
# Returns: [] (empty feed for new user)
```

## Common Mistakes

1. **Not including self in news feed**:
   ```python
   # Wrong: Only followings
   feed_candidates = self.network[userId]["followings"]
   
   # Correct: Include self
   feed_candidates = self.network[userId]["followings"].copy()
   feed_candidates.add(userId)
   ```

2. **Modifying the followings set directly**:
   ```python
   # Wrong: Modifies user's data
   self.network[userId]["followings"].add(userId)
   
   # Correct: Work with copy
   feed_candidates = self.network[userId]["followings"].copy()
   ```

3. **Wrong heap comparison**:
   ```python
   # Wrong: Min heap (oldest first)
   heapq.heappush(tweets, (time, ...))
   
   # Correct: Max heap (newest first)
   heapq.heappush(tweets, (-time, ...))
   ```

4. **Not handling index bounds**:
   ```python
   # Wrong: May go negative
   heapq.heappush(tweets, (..., index - 1))
   
   # Correct: Check bounds
   if index > 0:
       heapq.heappush(tweets, (..., index - 1))
   ```

## Design Trade-offs

### Storage Strategy
1. **Store all tweets** (current approach)
   - Pro: Complete history
   - Con: Unbounded memory growth

2. **Limit tweets per user** (deque with maxlen)
   - Pro: Bounded memory
   - Con: May lose old tweets

3. **Database with indexing**
   - Pro: Scalable, persistent
   - Con: More complex, slower

### Feed Generation
1. **K-way merge** (current approach)
   - Pro: Efficient for small k
   - Con: Slower for many followings

2. **Pre-computed timeline**
   - Pro: O(1) read
   - Con: Complex updates, more storage

3. **Pull vs Push model**
   - Pull (current): Generate on request
   - Push: Update followers' feeds on post

## Pattern Recognition

This problem demonstrates:
- **K-way merge** - Merging multiple sorted streams
- **System design basics** - Data modeling for social network
- **Heap for top-K** - Efficiently getting most recent items
- **Index tracking** - Traversing multiple lists simultaneously

Similar problems:
- Merge K Sorted Lists
- Design Facebook/Instagram Feed
- Top K Frequent Elements
- Design Search Autocomplete System

## Key Insights

1. **Global clock ensures ordering** - Timestamps guarantee chronological order across users

2. **K-way merge is optimal** - For k users with n tweets each, O(10 log k) beats O(kn log kn) sorting

3. **Index tracking avoids redundancy** - Store position in each user's tweet list

4. **Set for relationships** - O(1) follow/unfollow operations

5. **Lazy user creation** - Create users on demand rather than upfront

## What I Learned

The solution demonstrates how k-way merge can be applied to system design problems. The key insight is treating each user's tweets as a sorted stream and using a heap to efficiently merge them. The index tracking pattern allows us to traverse multiple lists without copying data. This design balances simplicity with efficiency - while a production system would need persistence and caching, the core algorithm of k-way merge for timeline generation remains fundamental to social media systems.