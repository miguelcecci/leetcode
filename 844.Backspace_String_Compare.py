class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = [], []
        def input_val(command, asdf):
            if command == '#':
                if len(asdf) == 0:
                    return []
                return asdf[:-1]
            return asdf+[command]
            
        for i in range(max(len(s), len(t))):
            if i < len(s):
                a = input_val(s[i], a)
            if i < len(t):
                b = input_val(t[i], b)
        
        return a == b
