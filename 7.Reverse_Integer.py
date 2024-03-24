class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        _reversed = str(x)[::-1]
        if '-' in _reversed:
            negative = True
            _reversed = _reversed.replace('-', '')
        
        _reversed = int(_reversed)
        if negative:
            _reversed = -1*_reversed

        if _reversed >= (2**31)-1:
            return 0
        
        if -2**31 >= _reversed:
            return 0

        return _reversed

