# coding: utf-8

import random
import numpy as np

jumlah = 10 #Number of customer in the system
it = [] #inter arrival rate
st = [] #service time

'''Generate the value of arrival rate and service time'''
for i in range(jumlah): 
    if i == 0:
        it.append(0)
        st.append(round(random.uniform(1, 4), 2))
    else:
        it.append(round(random.uniform(1, 4), 2))
        st.append(round(random.uniform(1, 4), 2))


'''Customer arrival rate'''
'''Customer service Time'''
arr = []
for i in range(jumlah):
    if i == 0:
        arr.append(it[i])
    else:
        arr.append(it[i-1]+it[i])
        if it[i] < st[i]:
            dep.append(dep[i-1] + st[i])
        else:
            dep.append(it[i-1] + it[i] + st[i])

'''
Below script is to show the event.
In my code, my i choose to give output an event because my professor ask me
You can simply change the output to what u want, by seeing the it[] and st[] first
to make u undestand easily.
'''
event = np.concatenate((arr, dep), axis=0)
event.sort()
for i in range(len(event)):
    print("Event ke: " + str(i+1) + " pada detik ke: " + str(event[i]))
