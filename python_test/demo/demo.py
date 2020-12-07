class test(object):

    def __init__(self, var1):
        self.var1 = var1

    def method(self):
        return self.var1

    def method2(self, param,a="aaa"):
        return a

    pass


t = test(1234)

result = t.method()
print(result)

val = 12
method_result = t.method2(val)
print(method_result)





