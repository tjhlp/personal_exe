"""
有 n 个人，每个人都有一个  0 到 n-1 的唯一 id 。

给你数组 watchedVideos  和 friends ，其中 watchedVideos[i]  和 friends[i] 分别表示 id = i 的人观看过的视频列表和他的好友列表。

Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 k 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。

给定你的 id  和一个 level 值，请你找出所有指定 level 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。

示例 1：
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]],
friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
输出：["B","C"]
解释：
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -> watchedVideos = ["C"] 
id 为 2 -> watchedVideos = ["B","C"] 
你朋友观看过视频的频率为：
B -> 1 
C -> 2
示例 2：
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
输出：["D"]
解释：
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
 
提示：
n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= id < n
1 <= level < n
如果 friends[i] 包含 j ，那么 friends[j] 包含 i

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-watched-videos-by-your-friends

"""

friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]

# id = 0
# level = 1
# res = []
# temp_friends_1 = []
# init_friends = friends[id]
# for i in range(1, level+1):
#
#     if i == 1:
#         temp_friends_1 = init_friends
#     else:
#         temp_friends_2 = []
#         for t in temp_friends_1:
#             for c in friends[t]:
#                 if c not in temp_friends_2:
#                     temp_friends_2.append(c)
#         else:
#             temp_friends_1 = temp_friends_2
# else:
#     if id in temp_friends_1:
#         temp_friends_1.remove(id)
#     print(temp_friends_1)
#     for j in temp_friends_1:
#         for d in watchedVideos[j]:
#             if d not in res:
#                 res.append(d)
# print(sorted(res, key=str.lower))

level = 1
id = 0
import collections
n = len(friends)
used = [False] * n
q = collections.deque([id])
used[id] = True
for _ in range(level):
    span = len(q)
    for i in range(span):
        u = q.popleft()
        for v in friends[u]:
            if not used[v]:
                q.append(v)
                used[v] = True

freq = collections.Counter()
for _ in range(len(q)):
    u = q.pop()
    for watched in watchedVideos[u]:
        freq[watched] += 1

videos = list(freq.items())
videos.sort(key=lambda x: (x[1], x[0]))

ans = [video[0] for video in videos]
print(ans)



