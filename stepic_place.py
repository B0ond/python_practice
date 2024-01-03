# дан массив неупорядочных чисел [1, 2, 4, 12, 6, 3, 7, 90, 5, 2, 0, 4] и число k
# нужно найти число из массива в сумме дающие k




class Solution(object):
    """HashSet solution"""
    def twoSumIndex(self, nums, target):
        num_set = {}
        for i, num in enumerate(nums):
            if target - num in num_set:
                return [num_set[target - num], i]
            num_set[num] = i

    def twoSumValues(self, nums, target):
        hash_set = []
        for i, enum_value in enumerate(nums):
            if target - enum_value in hash_set:
                return [target - enum_value, nums[i]]
            hash_set.append(enum_value)


out = Solution()
print(out.twoSumIndex([1, 32, 33, 12, 44, 3, 7, 90, 5, 5, 0, 4], 9))
print(out.twoSumValues([1, 32, 33, 12, 44, 3, 7, 90, 5, 5, 0, 4], 9))
