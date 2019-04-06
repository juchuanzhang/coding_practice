# MNIST数字识别问题
import tensorflow as tf
import os
# from tensorflow.examples.tutorials.mnist import input_data

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

v = tf.Variable(0, dtype=tf.float32, name="v")
ema = tf.train.ExponentialMovingAverage(0.99)

print(ema.variables_to_restore())

saver = tf.train.Saver(ema.variables_to_restore())

with tf.Session() as sess:
    saver.restore(sess, "/path/to/model/model.ckpt")
    print(sess.run(v))

