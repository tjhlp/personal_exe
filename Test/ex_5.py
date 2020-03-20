"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""


# 冒泡排序
# class Solution:
#     def getLeastNumbers(self, arr, k):
#         for i in range(0, len(arr)-1):
#             for j in range(i + 1, len(arr)):
#                 if arr[i] > arr[j]:
#                     arr[i], arr[j] = arr[j], arr[i]
#         return arr[:k]

class Solution:
    def getLeastNumbers(self, arr, k):
        arr.sort()
        return arr[:k]


s = Solution()
data_arr = [0, 1, 2, 2, 2, 1, 3, 6, 3, 1, 8, 2, 5, 3, 11, 4, 11, 12, 6, 2, 7, 19, 20, 16, 23, 6, 23, 4, 3, 25, 19, 15,
            15, 17, 26, 30, 24, 31, 2, 26, 32, 6, 27, 21, 3, 6, 18, 46, 14, 13, 43, 19, 17, 50, 46, 40, 13, 2, 10, 43,
            6, 5, 8, 23, 41, 21, 58, 10, 28, 22, 25, 63, 7, 40, 64, 50, 7, 57, 61, 43, 45, 64, 78, 50, 49, 15, 45, 10,
            27, 66, 14, 68, 81, 48, 51, 33, 17, 35, 71, 31]
data_k = 24
data = s.getLeastNumbers(data_arr, data_k)
print(data)
