class Solution:
    def romanToInt(self, s: str) -> int:
        roman_decimal_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        previous = None
        result = 0
        for roman_char in s:
            decimal_value = roman_decimal_dict[roman_char]

            if previous != None:
                if previous < decimal_value:
                    result = result - previous*2
            result = result + decimal_value
            previous = decimal_value
            
        return result
