class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.frequency += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.frequency

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        maxHeap = []
        for word in words:
            trie.insert(word)
        for word in words:
            heappush(maxHeap, (-1 * trie.search(word), word))
        output = []
        while k > 0:
            temp = heappop(maxHeap)[1]
            if temp not in output:
                output.append(temp)
                k -= 1
        return output