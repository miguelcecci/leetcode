class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_rows = numRows
        rows = []
        for i in range(num_rows): 
            rows.append('')
        
        direction = 1
        cursor = 0
        for i in s:
            print(cursor)
            rows[cursor] = rows[cursor]+i
            if cursor+direction < 0 or cursor+direction >= num_rows:
                direction = direction*(-1)
            cursor = cursor + direction

        result = ''
        for i in rows:
            result = result + i

        return result
        
