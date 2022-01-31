import random
from subprocess import NORMAL_PRIORITY_CLASS
from time import time, sleep
from listfactory import randomList, sortedList
from tqdm import tqdm
import matplotlib.pyplot as plt
from time import sleep

def selectionSort(myList):
    for i in range(len(myList)):
        minPoint = i
        for j in range(i+1, len(myList)):
            if myList[minPoint] > myList[j]:
                minPoint = j
        myList[i], myList[minPoint] = myList[minPoint], myList[i]



def draw(x, y):
	plt.plot(x, y, "b.")
	plt.draw()
	plt.pause(0.0001)
	plt.clf()


n_lis = []
time_lis = []
draw(0, 0)
for max_num in tqdm(range(200)):
    for sample in range(5):
        myList = randomList(max_num)
        start = time()                  
        for run in range(1000):
            selectionSort(myList)
        end = time()
    n_lis.append(max_num)
    time_lis.append(end-start)
    draw(n_lis, time_lis)

plt.plot(n_lis, time_lis, 'b.')
plt.show()