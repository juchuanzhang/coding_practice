# MNIST数字识别问题
# import tensorflow as tf
import os
from tensorflow.examples.tutorials.mnist import input_data

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mnist = input_data.read_data_sets("path/to/MNIST_data/", one_hot=True)

print("Training data size: ", mnist.train.num_examples)
print("Validating data size: ", mnist.validation.num_examples)
print("Testing data size: ", mnist.test.num_examples)
print("Example training data: ", mnist.train.images[0])
print("Example training data label: ", mnist.train.labels[0])
