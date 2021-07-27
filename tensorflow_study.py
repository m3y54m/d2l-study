#!/user/bin/env python3


# 2.1. Data Manipulation
# 2.1.1. Getting Started

import tensorflow as tf

# create a row vector x containing the first 12 integers starting with 0
x = tf.range(12)
print(x)

print(x.shape)

print(tf.size(x))

# change the shape of a tensor
X = tf.reshape(x, (3, 4))
print(X)

# create a tensor representing a tensor with all elements set to 0 and a shape of (2, 3, 4)
print(tf.zeros((2, 3, 4)))

# create tensors with each element set to 1
print(tf.ones((2, 3, 4)))

# create a tensor with shape (3, 4)
# each of its elements is randomly sampled from a standard Gaussian (normal) distribution
# with a mean of 0 and a standard deviation of 1.
print(tf.random.normal(shape=[3, 4]))
