"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
"""


class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            temp = nums[i]
            next_i = i + 1
            for j in range(next_i, len(nums)):
                temp += nums[j]
                if temp == k:
                    count += 1
                    break
        return count


s = Solution()
nums = [28, 54, 7, -70, 22, 65, -6]
k = 100
z = s.subarraySum(nums, k)
print(z)
