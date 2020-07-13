def demo(func):
    def insert():
        print('demo')
        return func()

    return insert


def demo_1():
    x = 8 / (1 + 1) * (3 + 2) - 1
    print(x)


if __name__ == '__main__':
    # demo_1()
    # print(len('2019-06-15,2019-07-01'))
    # print(eval('demo_1()'))
    # print(eval('demo_1()'))
    # print(eval('9/(1+1) *3+(3+2)'))
    dict_a = {"js1":123,"js2":5555}
    if "js3" and "js2" in dict_a:
        print(111)




