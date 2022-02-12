import numpy as np

a = np.random.rand(2, 3, 4, 5)
print("a shape", a.shape)
b = a.reshape(-1, 5)
print("b reshape", b.shape)
c = a.reshape(2, 3, -1)
print("c reshape", c.shape)
d = a.reshape(-1)
print("d reshape", d.shape)

f = a.transpose(1, 0, 2, 3)
print("f reshape", f.shape)

g = np.reshape(a, (-1, 3))
print("a reshape", g.shape)
