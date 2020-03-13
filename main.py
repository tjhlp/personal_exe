

def demo(func):

    def insert():
        print('demo')
        return func()

    return insert

@demo
def demo_1():
    print('demo_1')


if __name__ == '__main__':
    demo_1()