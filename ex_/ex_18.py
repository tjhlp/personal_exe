"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4


"""


class Solution:
    def singleNumber(self, nums) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i


list_1 = [2, 2, 1]
s = Solution()
res = s.singleNumber(list_1)
print(res)

from functools import reduce

# 使用异或解法
class Solution_1:
    def singleNumber(self, nums) -> int:
        return reduce(lambda x, y: x ^ y, nums)

list_2 = [1,2,1,2]
c = Solution_1()
res = c.singleNumber(list_2)
print(res)