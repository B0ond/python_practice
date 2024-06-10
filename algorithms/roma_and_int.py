class Solution:
    roman_nums = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                  ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

    def intToRoman(self, insert_nums: int, roman_nums=None) -> str:

        roman = ''
        while insert_nums:
            for roma_variable, int_variable in self.roman_nums:
                while insert_nums >= int_variable:
                    roman = roman + roma_variable
                    insert_nums = insert_nums - int_variable
        return roman

    def romainToInt(self, insert_roma: str) -> int:
        int_values = 0
        for roma_variable, int_variable in self.roman_nums:
            while insert_roma.startswith(roma_variable):
                int_values += int_variable
                insert_roma = insert_roma[len(roma_variable):]
        return int_values


x = Solution()
out_roman = x.intToRoman(94)
out_int = x.romainToInt('XCIV')
print(f'Из Арабского в Римский {out_roman}')
print(f'Из Римского в Арабский {out_int}')


# nums = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'LC': 90,
#         'C': 100, 'CD': 400, 'D': 500, 'DM': 900, 'M': 1000}
