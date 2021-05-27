import numpy as np
import matplotlib.pyplot as plt
import random


f = open('rr.txt', 'r')
rr_start_end = []
# with open('rr.txt') as f:
##    lines = f.readlines()

l = f.readline()
for i in range(int(l)):
    s = int(f.readline()[:-1])
    e = int(f.readline()[:-1])
    tup = (s, e)
    rr_start_end.append(tup)

rr_start_end.sort(key=lambda x: x[0])
print(rr_start_end)

img = plt.imread('khi.png')
plt.figure()
plt.axis([0, 1200, 0, 800])
implot = plt.imshow(img)

start = []
for j in range(len(rr_start_end)):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    tup = (x, y)
    start.append(tup)

    plt.scatter(x, y, color='red')
    plt.pause(int(rr_start_end[i][0])/10000)

for k in range(len(rr_start_end)):
    x = start[k][0]
    y = start[k][1]

    plt.scatter(x, y, color='green')
    plt.pause((int(rr_start_end[i][1]) - int(rr_start_end[i][0]))/20)
plt.show()

print(rr_start_end)


# plt.show()
