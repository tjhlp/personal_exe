"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        min_stack = self.stack[0]
        for i in self.stack:
            min_stack = i if i < min_stack else min_stack
        return min_stack


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
c = minStack.getMin()
minStack.pop()
minStack.top()
d = minStack.getMin()


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# list_1 = [1, 4, 3, 2, 3]
# list_1.pop(0)
# list_1.insert(0, 22)
# list_1.append(2)
# z = list_1.count(0)
# s = list_1.sort()
# print(s)
# list_1.remove(2)
# i = list_1.index(2)
# print(i)
# print(list_1)

dict_1 = {'a': '2', 'b': '1', 'c': '3'}
g = dict_1.get('a')
# print(g)
dict_1.pop('a')
dict_1.update({'a':'33'})
print(dict_1)

str1 = 'abc fddds'
# t = str1.split(' ')
zz = str1.index('f')
cou = str1.count('d')

print(cou)
print(zz)




