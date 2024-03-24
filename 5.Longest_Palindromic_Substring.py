class Solution:

    def longestPalindrome(self, s: str) -> str:

        def _is_palindromic(s: str) -> bool:
            return s == s[::-1]

        def _get_trio_indexes(s: str) -> list:
            trio_indexes = []
            for i in range(len(s)):
                prev = i-1
                next = i+1
                if prev >= 0 and next < len(s):
                    if s[prev] == s[next]:
                        trio_indexes.append(i)
            return trio_indexes
        
        def _get_pair_indexes(s: str) -> list:
            pair_indexes = []
            for i in range(len(s)):
                if i+1 < len(s):
                    if s[i+1] == s[i]:
                        pair_indexes.append(i)
            return pair_indexes
        
        def _get_full_size(s: str, p_index: int, pair: bool):
            final_string = s[p_index]
            
            prev = p_index-1
            if pair:
                final_string = ''
                prev = p_index

            next = p_index+1

            while next < len(s) and prev >= 0 and s[prev] == s[next]:
                final_string = s[prev] + final_string + s[next]
                prev = prev-1
                next = next+1

            return final_string

        result = []

        for i in _get_trio_indexes(s):
            result.append(_get_full_size(s, i, False))
        for i in _get_pair_indexes(s):
            result.append(_get_full_size(s, i, True))
        
        if len(result) == 0:
            return s[0]
        return max(result, key=len)
