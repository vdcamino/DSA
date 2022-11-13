class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        bucket = [TrieNode() for _ in range(len(words) + 1)]
        self.k = k

        def add_word(root, word):
            ptr = root
            for c in word:
                if c not in ptr.children:
                    ptr.children[c] = TrieNode()
                ptr = ptr.children[c]
            # we store the words in the trie itself to avoid passing prefixes through
            # the recursive calls and do multiple string operations, which is costly
            ptr.children["#"] = word

        # we get the words in lexicographic order because we perform preorder traversal
        def get_words(ptr) -> List[str]:
            if self.k == 0:
                return
            if "#" in ptr.children:
                self.k -= 1
                res.append(ptr.children["#"])
            for i in range(26):
                c = chr(ord("a") + i)
                if c in ptr.children:
                    get_words(ptr.children[c])

        # add words to the buckets; each bucket contains a trie
        for word, freq in cnt.items():
            add_word(bucket[freq], word)

        res = []
        for i in range(len(words), 0, -1):
            if self.k == 0:
                return res
            if bucket[i]:
                get_words(bucket[i])
        return res
