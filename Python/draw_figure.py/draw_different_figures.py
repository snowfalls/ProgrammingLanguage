import matplotlib.pyplot as plt
import numpy as np
import math

p = np.random.normal(size=1000000) # standard normal distribution

# 1000 bins means the 1000000 points will drop into 1 of the 1000 bins
plt.hist(p, bins=1000)
plt.show()


# this is a program to show how to draw a sin curve
x = []
y = []
for i in range(1000):
    i = i / 100
    x.append(i)
    t = math.sin(i)
    y.append(t)

plt.plot(x, y)
plt.show()


# this is a program to show how to draw (x-25)^2 with bar plot
z = []
w = []
for i in range(50):
    z.append(i)
    t = (i - 25) * (i - 25)
    w.append(t)


plt.bar(z, w)
plt.show()
