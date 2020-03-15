"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island

"""
import collections


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        r = len(grid)
        islands = []
        edges = []
        if r == 0:
            return 0
        c = len(grid[0])
        for i in grid:
            i.append(0)
        grid.append([0] * c)
        ans = 0
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if grid[i][j] == 1:
                    island = [[i, j]]
                    islands.append(island)
                    grid[i][j] = len(islands)
                    if grid[i + 1][j] > 0:
                        edges.append([[i, j], [i + 1, j]])
                    if grid[i][j + 1] > 0:
                        edges.append([[i, j], [i, j + 1]])
        if len(islands) > 0:
            ans = 1
        while len(edges) > 0:
            edge = edges.pop()
            newislandid = grid[edge[0][0]][edge[0][1]] - 1
            oldislandid = grid[edge[1][0]][edge[1][1]] - 1
            if newislandid == oldislandid:
                continue
            if len(islands[newislandid]) < len(islands[oldislandid]):
                newislandid, oldislandid = oldislandid, newislandid
            for i in islands[oldislandid]:
                grid[i[0]][i[1]] = newislandid + 1
                islands[newislandid].append(i)
            islands[oldislandid] = []
            if ans < len(islands[newislandid]):
                ans = len(islands[newislandid])

        return ans


# class Solution:
#     def maxAreaOfIsland(self, grid):
#         max_area = 0
#         for rows in grid:
#             temp_ = dict(collections.Counter(rows))
#             if max_area < temp_[1]:
#                 max_area = temp_[1]
#         return max_area


data = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

data1 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]



s = Solution()
t = s.maxAreaOfIsland(data1)
print(t)
