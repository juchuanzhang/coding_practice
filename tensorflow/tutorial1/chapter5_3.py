# MNIST数字识别问题
import tensorflow as tf
# import os


# with tf.variable_scope("foo"):
#     v = tf.get_variable(
#         "v", [1], initializer=tf.constant_initializer(1.0))

# with tf.variable_scope("foo"):
#     v = tf.get_variable("v", [1])
# with tf.variable_scope("foo", reuse=True):
#     v1 = tf.get_variable("v", [1])
#     print(v == v1)
# with tf.variable_scope("bar", reuse=True):
#     v = tf.get_variable("v", [1])

# with tf.variable_scope("root"):
#     print(tf.get_variable_scope().reuse)

v1 = tf.get_variable("v", [1])
print(v1.name)

with tf.variable_scope("foo"):
    v2 = tf.get_variable("v", [1])
    print(v2.name)

with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v3 = tf.get_variable("v", [1])
        print(v3.name)

    v4 = tf.get_variable("v1", [1])
    print(v4.name)

with tf.variable_scope("", reuse=True):
    v5 = tf.get_variable("foo/bar/v", [1])

    print(v5 == v3)
    v6 = tf.get_variable("foo/v1", [1])
    print(v6 == v4)
