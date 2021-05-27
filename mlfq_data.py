mlfq_start_end = []
f = open('mlfq1.txt', 'r')

# with open('rr.txt') as f:
##    lines = f.readlines()

l1 = f.readline()
for i in range(int(l1)):
    p1 = int(f.readline()[:-1])
    p2 = int(f.readline()[:-1])
    p3 = int(f.readline()[:-1])
    d = int(f.readline()[:-1])
    tup = (p1, p2, p3, d)
    mlfq_start_end.append(tup)

f = open('mlfq2.txt', 'r')

l2 = f.readline()
for j in range(int(l2)):
    p1 = int(f.readline()[:-1])
    p2 = int(f.readline()[:-1])
    p3 = int(f.readline()[:-1])
    d = int(f.readline()[:-1])
    tup = (p1, p2, p3, d)
    mlfq_start_end.append(tup)

for k in mlfq_start_end:
    print(k)

with open("mlfq.txt", 'w') as output:
    output.write(str(len(mlfq_start_end)))
    output.write('\n')
    for i in range(len(mlfq_start_end)):
        output.write(str(mlfq_start_end[i][0]))
        output.write('\n')
        output.write(str(mlfq_start_end[i][1]))
        output.write('\n')
        output.write(str(mlfq_start_end[i][2]))
        output.write('\n')
        output.write(str(mlfq_start_end[i][3]))
        output.write('\n')
