import time
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

import mnist_inference
import mnist_train

# 没10秒加载一次最新的模型，并在测试数据上测试最新模型的正确率
EVAL_INTERVAL_SECS = 10
BATCH_SIZE = 5000

def evaluate(mnist):
    with tf.Graph().as_default() as g:
        # 定义输入输出的格式
        x = tf.placeholder(tf.float32, [BATCH_SIZE,
                                        mnist_inference.IMAGE_SIZE,
                                        mnist_inference.IMAGE_SIZE,
                                        mnist_inference.NUM_CHANNELS],
                           name="x-input")
        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')
        xs = mnist.validation.images
        reshaped_xs = np.reshape(xs, (BATCH_SIZE,
                                     mnist_inference.IMAGE_SIZE,
                                     mnist_inference.IMAGE_SIZE,
                                     mnist_inference.NUM_CHANNELS))
        validate_feed = {x: reshaped_xs, y_: mnist.validation.labels}
        y = mnist_inference.inference(x, False, None)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        # 每隔EVAL_INTERVAL_SECS秒调用一次计算正确率的过程以检测训练过程中正确率的变化
        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    # 加载模型
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print("After %s training step(s), validation accuracy = %g" % (global_step, accuracy_score))
                else:
                    print("No checkpoint file found")
                    return
            time.sleep(EVAL_INTERVAL_SECS)


def main(args=None):
    mnist = input_data.read_data_sets("/path/to/mnist_data", one_hot=True)
    evaluate(mnist)


if __name__ == "__main__":
    tf.app.run()
