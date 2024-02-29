class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "C":
                record = record[:-1]
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "+":
                score_sum = record[-1] + record[-2]
                record.append(score_sum)
            else:
                record.append(int(i))
        return sum(record)
