from keras.datasets import fashion_mnist
(train_X,train_Y),(test_X,test_Y) = fashion_mnist.load_data()


import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt

#%matplotlib inline

print('Training data shape: ',train_X.shape,train_Y.shape)
print('Testing data shape: ',test_X.shape,test_Y.shape)
