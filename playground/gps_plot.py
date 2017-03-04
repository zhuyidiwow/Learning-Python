import numpy as np
import matplotlib.pyplot as plt


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


fh = open("gps_data.txt")

X = list()
Y = list()

for line in fh:
    fragments = line.split(",")
    x = float(fragments[0])
    y = float(fragments[1])
    X.append(x)
    Y.append(y)

x = np.array([58, 0, 20, 2, 2, 0, 12, 17, 16, 6, 257, 0, 0, 0, 0, 1, 0, 13, 25,
              9, 13, 94, 0, 0, 2, 42, 83, 0, 0, 157, 27, 1, 80, 0, 0, 0, 0, 2, 
              0, 41, 0, 4, 0, 10, 1, 4, 63, 6, 0, 31, 3, 5, 0, 61, 2, 0, 0, 0, 
              17, 52, 46, 15, 67, 20, 0, 0, 20, 39, 0, 31, 0, 0, 0, 0, 116, 0, 
              0, 0, 11, 39, 0, 17, 0, 59, 1, 0, 0, 2, 7, 0, 66, 14, 1, 19, 0, 
              101, 104, 228, 0, 31])

y = np.array([60, 0, 9, 1, 3, 0, 13, 9, 11, 7, 177, 0, 0, 0, 0, 1, 0, 12, 31, 
              10, 14, 80, 0, 0, 2, 30, 70, 0, 0, 202, 26, 1, 96, 0, 0, 0, 0, 1,
              0, 43, 0, 6, 0, 9, 1, 3, 32, 6, 0, 20, 1, 2, 0, 52, 1, 0, 0, 0, 
              26, 37, 44, 13, 74, 15, 0, 0, 24, 36, 0, 22, 0, 0, 0, 0, 75, 0, 
              0, 0, 9, 40, 0, 14, 0, 51, 2, 0, 0, 1, 9, 0, 59, 9, 0, 23, 0, 80,
              81, 158, 0, 27])

N = len(x)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, c=colors, alpha=0.5)

# n = 1024
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(Y, X)

# plt.axes([0.025, 0.025, 0.95, 0.95])
# plt.scatter(X, Y, s=1, c=T, alpha=.5)

# plt.xlim(-5, 5), plt.xticks([])
# plt.ylim(-5, 5), plt.yticks([])
# savefig('../figures/scatter_ex.png',dpi=48)
plt.show()
