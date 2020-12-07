"""
协程
yield 生成器
1.包含yield的函数,则是一个可迭代对象
2.生产者消费者行为
3.无需立即执行,需要时在执行
4.斐波那契数列


"""


def test():
    a = 10
    i = 0
    while i < a:
        x = yield i
        i += 1


print(test())
t=test()
print(type(t))
# for i in test():
#     print(i)
