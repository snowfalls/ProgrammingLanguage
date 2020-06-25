#######################################################################
# This is a python program to demonstrate the python division 
# Python supports tensors division

import numpy as np


a = np.random.rand(3, 3)
b = np.array([[1], [2], [3]])

print("original a:\n", a)
print("\noriginal b:\n", b)

print("\na/b\n", a/b)