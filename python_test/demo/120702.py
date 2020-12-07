import sys
import logging

system = sys.exc_info()
print(system)

log = logging.info(system)
print(log)
print(sys)

# twisted  框架
"""
先断言绝对不能发生的错误
然后再去处理错误(异常)
"""

try:
    print()
except:
    print()
finally:
    print()
