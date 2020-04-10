from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        # number of words with this prefix
        self.num_prefixes = 0
        # number of words ending at this node
        self.num_words = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        current.num_prefixes += 1 # for the root node
        for c in word:
            if not current.nodes[c]:
                current.nodes[c] = TrieNode()
            current = current.nodes[c]
            current.num_prefixes += 1
        current.num_words += 1


def recurse(root, group_size, length):
    if root.num_prefixes < group_size:
        return 0
    here = root.num_words
    ans = 0
    for c, node in root.nodes.items():
        ans += recurse(node, group_size, length+1)
        here += node.num_prefixes % group_size
    ans += (here // group_size) * length
    return ans


def solve():
    # N = num strings, K = group size
    N, K = map(int, input().split(" "))
    trie = Trie()
    for i in range(N):
        s = input()
        trie.insert(s)
    return "{}".format(recurse(trie.root, K, 0))
    

t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))