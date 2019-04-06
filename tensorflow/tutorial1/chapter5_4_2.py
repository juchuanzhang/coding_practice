# MNIST数字识别问题
import tensorflow as tf
import os
# from tensorflow.examples.tutorials.mnist import input_data

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

saver = tf.train.import_meta_graph("/path/to/model/model.ckpt.meta")
with tf.Session() as sess:
    saver.restore(sess, "/path/to/model/model.ckpt")
    print(sess.run(tf.get_default_graph().get_tensor_by_name("add:0")))
