class Solution:

    def romainToInt(self, s:str) -> int:
        nums = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'LC': 90,
                'C': 100, 'CD': 400, 'D': 500, 'DM': 900, 'M': 1000}
        summa = 0
        for i in s:
            summa += nums.get(i)
        return summa


x = Solution()
out = x.romainToInt('MCMXCIV')
print(out)