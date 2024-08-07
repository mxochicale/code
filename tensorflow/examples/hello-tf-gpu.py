## github.com/j-min/test_single_gpu.py
## https://gist.github.com/j-min/baae1aa56e861cab9831b3722755ae6d


from __future__ import print_function
'''
Basic Multi GPU computation example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

'''
This tutorial requires your machine to have 1 GPU
"/cpu:0": The CPU of your machine.
"/gpu:0": The first GPU of your machine
'''

import numpy as np
import datetime

# Processing Units logs
log_device_placement = True


import numpy as np
import datetime
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() #https://github.com/theislab/scgen/issues/14


## Number of multiplications to perform
n=10


'''
Example: compute A^n + B^n on 2 GPUs
Results on 8 cores with 2 GTX-980:
 * Single GPU computation time: 0:00:11.277449
 * Multi GPU computation time: 0:00:07.131701
'''

# Create random large matrix
A = np.random.rand(10000, 10000).astype('float32')
B = np.random.rand(10000, 10000).astype('float32')

# Create a graph to store results
c1 = []
c2 = []

'''
Single GPU computing
'''
with tf.device('/gpu:0'):
    a = tf.placeholder(tf.float32, [10000, 10000])
    b = tf.placeholder(tf.float32, [10000, 10000])
    # Compute A^n and B^n and store results in c1
    c1.append(tf.pow(a, n))
    c1.append(tf.pow(b, n))

with tf.device('/cpu:0'):
  sum = tf.add_n(c1) #Addition of all elements in c1, i.e. A^n + B^n

t1_1 = datetime.datetime.now()
with tf.Session(config=tf.ConfigProto(log_device_placement=log_device_placement)) as sess:
    # Run the op.
    sess.run(sum, {a:A, b:B})
t2_1 = datetime.datetime.now()

print("Single GPU computation time: " + str(t2_1-t1_1))

