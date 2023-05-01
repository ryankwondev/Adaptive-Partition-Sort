import matplotlib.pyplot as plt
import numpy as np

f = open("avgt.txt", 'r')
avgt = eval(f.readline())[0:501]
f.close()

f = open("maxt.txt", 'r')
maxt = eval(f.readline())[0:501]
f.close()

f = open("mint.txt", 'r')
mint = eval(f.readline())[0:501]
f.close()

t = np.arange(0, 501)

plt.plot(t, maxt, '-b', label='worst case')
plt.plot(t, avgt, 'r', label='average')
plt.plot(t, mint, '-g', label='best case')
plt.show()