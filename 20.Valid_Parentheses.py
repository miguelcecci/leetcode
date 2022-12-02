class Solution:

    def isValid(self, s: str) -> bool:
        strings = s
        for i in range(len(s)):
            strings = strings.replace("()", "").replace("[]", "").replace("{}", "")
        if strings == "":
            return True
        return False
