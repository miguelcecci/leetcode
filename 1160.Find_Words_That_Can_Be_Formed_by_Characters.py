class Solution:
    def checkGoodWord(self, word, chars):
        for letter in word:
            if letter in chars:
                chars = chars.replace(letter, "", 1)
            else:
                return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        result_count = 0
        for word in words:
            if self.checkGoodWord(word, chars):
                result_count = result_count + len(word)
        
        return result_count
