class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def check_and_merge(a, b):
            if a[1] >= b[0]:
                return [[a[0], b[1]]], True
            return [a, b], False

        counter = 0
        while counter+1 < len(intervals):
            result, merged = check_and_merge(intervals[counter], intervals[counter+1])
            intervals = intervals[:counter] + result + intervals[counter+2:]
            if merged:
                counter = 0
            counter = counter + 1
        
        return intervals
            
