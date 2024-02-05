class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        acc = 1
        for i in range(len(digits)-1, -1, -1):
            if acc == 1:
                digits[i] = digits[i] + 1
                acc = 0
                if digits[i] >= 10:
                    digits[i] = digits[i] - 10
                    acc = 1
            else:
                return digits
            if i == 0 and acc == 1:
                return [1] + digits
        return digits
