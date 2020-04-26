"""
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。
示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxDistance(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        result = []
        for i in range(m):
            for w in range(n):
                if grid[i][w] == 1:
                    result.append((i, w))
                else:
                    grid[i][w] = 0
        if len(result) == 0 or len(result) == m * n:
            return -1
        count = 0
        while result:
            count += 1
            for i in range(len(result)):
                x, y = result.pop(0)
                if x + 1 < m and grid[x + 1][y] == 0:
                    result.append((x + 1, y))
                    grid[x + 1][y] = -1
                if x - 1 >= 0 and grid[x - 1][y] == 0:
                    result.append((x - 1, y))
                    grid[x - 1][y] = -1
                if y + 1 < n and grid[x][y + 1] == 0:
                    result.append((x, y + 1))
                    grid[x][y + 1] = -1
                if y - 1 >= 0 and grid[x][y - 1] == 0:
                    result.append((x, y - 1))
                    grid[x][y - 1] = -1
        return count - 1


s = Solution()
res = s.maxDistance([[1, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
print(res)
