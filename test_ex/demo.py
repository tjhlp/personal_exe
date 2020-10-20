class Demo():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y


def demo_1(x, y):
    d = Demo(x, y)
    return d
