import matplotlib.pyplot as plt
x = ['1st', '2nd', '3rd']
f = open('mlfq.txt', 'r')
h = []
l = f.readline()
l = int(l)
for i in range(l):
    p1 = int(f.readline()[:-1])
    p2 = int(f.readline()[:-1])
    p3 = int(f.readline()[:-1])
    d = int(f.readline()[:-1])
    tup = (p1, p2, p3, d)
    h.append(tup)


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


plt.title('Real-Time Life Support')
plt.xlabel('Priority')
plt.ylabel('No. of Patients')

for j in range(len(h)):
    height = h[j][2], h[j][1], h[j][0]
    print(height)
    plt.bar(x, height, color='red')
    plt.pause((h[i][3])/1000)
    plt.bar(x, height, color='white')

addlabels(x, height)

plt.show()
