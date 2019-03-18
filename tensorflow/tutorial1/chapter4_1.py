import tensorflow as tf
from numpy.random import RandomState
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# a = tf.constant([1, 2], name="a", dtype=tf.float32)
# b = tf.constant([2.0, 3.0], name="b")
# result = a + b
# print(result)
# with tf.Session() as sess:
#     print(result.eval())
    # print(sess.run(result))
# print(result)
# sess = tf.Session()
# with sess.as_default():
#     print(result.eval())
# print(sess.run(result))
# print(result.eval(session=sess))
# config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
# sess1 = tf.InteractiveSession(config=config)
# sess2 = tf.Session(config=config)

batch_size = 8
w1 = tf.Variable(tf.random_normal((2, 3), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal((3, 1), stddev=1, seed=1))
# x = tf.constant([[0.7, 0.9]])
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")
a = tf.nn.relu(tf.matmul(x, w1) + biases1)
y = tf.nn.relu(tf.matmul(a, w2) + biases2)
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
    + (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))
learning_rate = 0.001
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    print(sess.run(w1))
    print(sess.run(w2))

    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            # 每隔一段时间计算所有数据上的交叉熵并输出。
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={x: X, y_: Y})
            print("After %d training step(s), cross entropy on all data is %g"
                 % (i, total_cross_entropy))
            print(sess.run(w1))
            print(sess.run(w2))

# sess = tf.Session()
# # sess.run(w1.initializer)
# # sess.run(w2.initializer)
# init_op = tf.global_variables_initializer()
# sess.run(init_op)
# # print(sess.run(y))
# print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
# sess.close()
