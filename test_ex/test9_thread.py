from concurrent.futures import ThreadPoolExecutor
import time

ar = ['filepath', 'thu1']

executor = ThreadPoolExecutor(10)


def doFileParse(filepath, segment, wordslist):
    try:

        time.sleep(wordslist)
    except Exception as e:
        return {'wordslist': '11111'}
    return {'wordslist': wordslist}


def p_call_back(res):
    res = res.result()  # !取到res结果 【回调函数】带参数需要这样
    print('%s' % (res['wordslist']))
    print('*' * 10)

for i in range(0, 4):
    ar.append(i)
    print(ar)
    # newTask = executor.submit(lambda p: doFileParse(*p), ar).add_done_callback(p_call_back)
    newTask = executor.submit(lambda p: doFileParse(*p), ar)
    ar = ['filepath', 'thu1']
    # print(newTask)

# print(111)
