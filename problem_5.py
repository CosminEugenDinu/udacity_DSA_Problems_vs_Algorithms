

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()    
        
    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        
        for char in word:
            if node.children.get(char):
                node = node.children.get(char)
#             node.children[char] = TrieNode()
            else:
                node.insert(char)
                node = node.children[char]
            
        node.is_word = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        
        for char in prefix:
            if node.children.get(char):
                node = node.children.get(char)
            else:
                return None
        return node

        
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        all_suffixes = []
        for char in self.children:
            next_node = self.children[char]
            if next_node.is_word:
                all_suffixes.append(suffix + char)
            all_suffixes += next_node.suffixes(suffix + char)
        
        return all_suffixes

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            return prefixNode.suffixes()

test_cases = [
    ["fan", None], 
    ["f", ["un", "unction", "actory"]],
    ["fu", ["n", "nction"]],
    ["tripod", []],
]

def test():
    for test_case in test_cases:
        prefix, result = test_case
        assert f(prefix) == result

# test()