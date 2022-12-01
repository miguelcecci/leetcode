class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = ""

        if len(strs) == 1:
            return strs[0]
        
        for i in range(1,200):

            prefixes = list(set([p[:i] for p in strs]))
            
            if len(prefixes) == 1:
                lcp = prefixes[0]
            else:
                return lcp
            
        return lcp
