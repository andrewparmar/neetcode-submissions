from dataclasses import dataclass, field

@dataclass
class TrieNode:
    word_end: bool = False
    children: Dict[str, TrieNode] = field(default_factory=dict)

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return True
        