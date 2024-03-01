class Solution:
    def removeStars(self, s: str) -> str:
        if not '*' in s:
            return s
        b = []
            
        for i in s:
            if i == '*':
                b.pop()
            else:
                b.append(i)
        return ''.join(b)
