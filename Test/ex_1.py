"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element

"""

import collections


class Solution:
    def majorityElement(self, nums):
        length = len(nums) / 2
        dict_a = {}
        print(length)
        if length < 1:
            return nums[0]

        for i in nums:
            if i in dict_a:
                dict_a[i] += 1
                if dict_a[i] > length:
                    return i
            else:
                dict_a[i] = 1


s = Solution()
print(s.majorityElement([6, 5, 5]))
nums = [6, 5, 5]
# best solution
res = [k for k, v in collections.Counter(nums).items() if v > len(nums) // 2][0]
print(res)
c1 =collections.Counter([2, 3, 4, 5, 6, 4, 3, 2, 4, 5])
print(dict(c1))
