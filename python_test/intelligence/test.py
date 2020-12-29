import cv2
import codecs, sys
import cgi
import os
import tensorboard
import tensorflow as tf
import PyQt5

a = tf.constant(1)
b = tf.constant(2)
result = a + b
print(result)
print(a - b)

import tensorflow as tf
from tensorflow.keras import layers, losses, metrics, optimizers


# 打印时间分割线
@tf.function
def printbar():
    ts = tf.timestamp()
    today_ts = ts % (24 * 60 * 60)

    hour = tf.cast(today_ts // 3600 + 8, tf.int32) % tf.constant(24)
    minite = tf.cast((today_ts % 3600) // 60, tf.int32)
    second = tf.cast(tf.floor(today_ts % 60), tf.int32)

    def timeformat(m):
        if tf.strings.length(tf.strings.format("{}", m)) == 1:
            return (tf.strings.format("0{}", m))
        else:
            return (tf.strings.format("{}", m))

    timestring = tf.strings.join([timeformat(hour), timeformat(minite),
                                  timeformat(second)], separator=":")
    tf.print("==========" * 8, end="")
    tf.print(timestring)


# 样本数量
n = 800

# 生成测试用数据集
X = tf.random.uniform([n, 2], minval=-10, maxval=10)
w0 = tf.constant([[2.0], [-1.0]])
b0 = tf.constant(3.0)
Y = X @ w0 + b0 + tf.random.normal([n, 1], mean=0.0, stddev=2.0)  # @表示矩阵乘法,增加正态扰动

# 构建输入数据管道
ds = tf.data.Dataset.from_tensor_slices((X, Y)) \
    .shuffle(buffer_size=1000).batch(100) \
    .prefetch(tf.data.experimental.AUTOTUNE)

# 定义优化器
optimizer = optimizers.SGD(learning_rate=0.001)
