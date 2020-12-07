def method(a, b=None):
    bo = isinstance(a, int)
    return bo
def method2(param):
    return isinstance(param,str)

result = method('11',1)
print(result)
print(method2("123"))

