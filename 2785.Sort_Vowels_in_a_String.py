class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {
            'A': 0, 'E': 0, 'I': 0, 'O': 0,
            'U': 0, 'a': 0, 'e': 0, 'i': 0,
            'o': 0, 'u': 0,
        }

        vowel_list = []
        a = s
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels.keys():
                vowels[s[i]] = vowels[s[i]] + 1
                s[i] = "_"
        
        vowel_list = "".join([x*y for x, y in vowels.items()])
        for i in range(len(s)):
            if s[i] == '_':
                s[i] = vowel_list[0]
                vowel_list = vowel_list[1:]

        return "".join(s)
