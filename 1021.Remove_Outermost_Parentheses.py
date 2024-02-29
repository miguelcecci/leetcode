class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level = 0
        final_string = ""

        for i in s:
            if i == '(':
                level += 1
            if level != 1:
                final_string = final_string + i
            if i == ')':
                level -= 1
        
        return final_string
        
