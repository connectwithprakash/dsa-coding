# First attempt
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        count = {}
        # Get counts of each word and store in a hash
        for word in words:
            count[word] = count.get(word, 0) + 1
        # Sort the keys by frequency
        count = [k for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)]
        return count[:k]


# Second Attempt: Using heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        # Get counts of each word and store in a hash
        for word in words:
            count[word] = count.get(word, 0) + 1
        # Create a order for sorting
        count = [(-v, k) for k, v in count.items()]
        heapq.heapify(count)
        
        return [heapq.heappop(count)[1] for _ in range(k)]

