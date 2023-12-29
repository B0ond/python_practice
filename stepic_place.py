
class Solution(object):
    def twoSum(self, nums, target):
        hash_set = {}
        for i, num in enumerate(nums):
            if target - num in hash_set:
                return [hash_set[target - num], i]
            hash_set[num] = i

out = Solution()

try:
    print(out.twoSum([3, 2, 4, 1, 2, 3, 5], 9))
except IndexError:
    print("Out of range")