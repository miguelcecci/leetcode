class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        possibilities = []
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):

                    if k < len(s):
                        # checking if all value are valid
                        valid = True
                        for value in (s[:i], s[i:j], s[j:k], s[k:]):
                            if value == '':
                                valid = false
                            if len(value) != 1 and value[0] == '0':
                                valid = False
                            if int(value) > 255:
                                valid = False

                        if valid:
                            possibilities.append(".".join([s[:i], s[i:j], s[j:k], s[k:]]))

        return possibilities

