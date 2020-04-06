from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for c in word:
            if not current.node[c]:
                current.node[c] = TrieNode()
            current = current.node[c]
        current.word = word

    def _prefix_helper(self, node, count):
        # if branch out or reach the end of a trie branch
        if len(node.node) > 1 or len(node.node) == 0:
            return count
        for c, n in node.node.items():
            count += 1
            return self._prefix_helper(n, count)

    def prefix_length(self):
        current = self.root
        count = 0
        return self._prefix_helper(current, count)



def solve():
    # N = num strings, K = group size
    N, K = map(int, input().split(" "))
    strs = []
    for i in range(N):
        strs.append(input())
    strs.sort()
    j = 0
    ans = 0
    while j < N:
        trie = Trie()
        for k in range(K):
            trie.insert(strs[j+k])
        ans += trie.prefix_length()
        j += K
    return "{}".format(ans)

t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))