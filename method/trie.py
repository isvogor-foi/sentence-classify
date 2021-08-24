from misc.load_data import get_ngram
from misc.stopwatch import stopwatch


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        node.counter += 1

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.dfs(node, x[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)


@stopwatch("Trie")
def run(sentences, categories, repeat=100):
    t = Trie()
    for category in categories:
        t.insert(category)

    for k in range(repeat):
        for sentence in sentences:
            _categories = []
            for word in get_ngram(sentence, 1):
                result = t.query(word)
                if len(result) > 0 and len(word) / len(result[0]) > 1:
                    _categories.append(result[0][0])
            # print(f"{sentence} in {_categories}")
