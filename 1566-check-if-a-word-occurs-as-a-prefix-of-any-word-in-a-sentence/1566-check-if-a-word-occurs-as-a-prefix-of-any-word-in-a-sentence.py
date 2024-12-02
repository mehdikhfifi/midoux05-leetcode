class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        

        sentence = sentence.split(' ')

        for index, word in enumerate(sentence):
            if searchWord == word[:len(searchWord)]:
                return index + 1
        return -1


