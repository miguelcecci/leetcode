class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def merge(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]
        
        # the line bellow is considered cheating
        intervals.sort(key=lambda x: x[0]) #sorting by the first value
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            a = result[-1]
            b = intervals[i]
            if a[1] >= b[0]:
                result[-1] = merge(a, b)
            else:
                result.append(b)
                
        return result
