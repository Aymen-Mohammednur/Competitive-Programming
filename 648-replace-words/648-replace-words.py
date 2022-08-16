class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.word:
                return curr.word
            if char not in curr.children:
                return word
            curr = curr.children[char]
        return curr.word if curr.word else word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        s = sentence.split()
        result = []
        for word in s:
            result.append(trie.search(word))
        return " ".join(result)