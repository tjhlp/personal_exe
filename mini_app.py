from multiprocessing import Process
from threading import Thread
import time
import gevent


def test1():
    for i in range(3):
        print('test1....', i)
        # time.sleep(0.2)
        gevent.sleep(0.2)


def test2():
    for i in range(3):
        print('test2....', i)


if __name__ == '__main__':
    p1 = Process(target=test1)
    p2 = Process(target=test2)
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    # p1.start()
    # p2.start()
    # t1.start()
    # t2.start()
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2)
    ]
    )
