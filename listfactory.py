import random

def randomList(n):
  l = list(range(n))
  random.shuffle(l)
  return l
  
def sortedList(n):
  return list(range(n))