"""
给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]


"""


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        nums_list = []
        for i in nums1:
            for j in nums2:
                nums_list.append((i + j, [i, j]))

        d = sorted(nums_list, key=lambda nums_list:nums_list[0])
        res = [x[1] for x in d]
        if k >= len(res):
            return res
        return res[:k]

# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
z = Solution()
res = z.kSmallestPairs(nums1, nums2, k)
print(res)