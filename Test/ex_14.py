"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
c = itertools.permutations('ABCD')

# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))


flag = list(itertools.permutations('+- */'))
print(len(flag))
temp = []
for i in flag:
    if i not in temp:
        temp.append(i)
    print(i)
print(len(temp))
