import random

for i in range(26):
    r = random.randint(1, 10)
    print('process'+chr(i+65)+' = Process('+"'" +
          chr(i+65)+"'"+', '+str(i)+', '+str(r)+')')
