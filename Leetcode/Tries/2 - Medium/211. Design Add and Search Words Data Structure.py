class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.trie
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['*'] = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        current = [self.trie]
        for ind,letter in enumerate(word):
            c = []
            for i in current:
                if letter!='.' and letter not in i:
                    continue
                elif letter!='.' and letter in i:
                    c.append(i[letter])
                elif letter=='.':
                    for j in i:
                        if j!='*':
                            c.append(i[j])
            current = c
            
            if len(current)==0:
                return False
        if True in current:
            return True
        for j in current:
            if '*' in j:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
