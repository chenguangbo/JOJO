"""
多线程
进程
pid  进程的唯一性

python里的多线程,不是真正意义上的多线程
    全局锁机制
    在任意指定的时间里,有且只有一个线程在运行
    GIL  全局锁
            线程安全的






"""
# coding=utf-8

import threading as th
import time

lock = th.Lock


def test():
    # time.sleep(10);
    lock.acquire()  # 加锁
    print(1)
    lock.release()  # 释放锁


a = th.Thread(target=test)
a.start()
a.join()


def a():
    for i in xrange(0, 10):
        print(i)
