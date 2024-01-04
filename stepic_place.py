# дан массив неупорядочных чисел [1, 2, 4, 12, 6, 3, 7, 90, 5, 2, 0, 4] и число k
# нужно найти число из массива в сумме дающие k


class Solution:
    @staticmethod
    def find_sum_index(arr: list[int], k: int) -> list[int]:
        set_num = {}
        for idx, values in enumerate(arr):
            if k - values in set_num:
                return [set_num[k - values], idx]
            set_num[values] = idx

    @staticmethod
    def find_sum(arr: list[int], k: int) -> list[int]:
        set_num = []
        for values in arr:
            if k - values in set_num:
                return [values, k-values]
            set_num.append(values)


arr_values = [1, 20, 4, 12, 6, 70, 7, 90, 5, 2, 0, 4]
k_values = 9
print(f"Индекс искомых хначений: {Solution.find_sum_index(arr_values, k_values)}")
print(f"Сами числа: {Solution.find_sum(arr_values, k_values)}")
