# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

#zad2
from array import *

tabZnakow = array('u',[])
print("Podaj znaki(string):")
znaki = str(input());

for i in range(0, len(znaki)):
    tabZnakow.append(znaki[i])

tabZnakow.reverse()

for i in tabZnakow:
    print(i)

#zad3
from array import *
import random

tabRand = array('f',[])
for i in range(0, 7):
    tabRand.append(random.uniform(-5,5))

try:
    file = open("result.txt","w")
    for i in tabRand:
        file.write(str(i)+", ")
finally:
    file.close()

#zad4
import numpy as np

mainArray = np.array([[2,3,4,5,6],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], np.int64)

for i in range(0,5):
    mainArray[1,i] = mainArray[0,i] ** 2
    mainArray[2,i] = mainArray[1,i] ** 2
    mainArray[3,i] = mainArray[2,i] ** 2
    mainArray[4,i] = mainArray[3,i] ** 2

for i in range(0,5):
    print(str(mainArray[i,0])+", "+str(mainArray[i,1])+", "+str(mainArray[i,2])+", "+str(mainArray[i,3])+", "+str(mainArray[i,4]))

#zad5
def histogram(lok):
    try:
        file = open(str(lok), "r")
        znaki = list(file.read())
        dict = {i:znaki.count(i) for i in znaki}
        print(dict)
    finally:
        file.close()

histogram("document.txt")

#zad6
import random
def deck():
    talia = []
    rangi = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    kolory = ['c','d','h','s']
    for i in rangi:
        for l in kolory:
            talia.append((i,l))
    return talia

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal(deck,n):
    stolik = []
    for i in range(0,n):
        stolik.append(random.sample(deck,5))
    return stolik

talia = deck()
potasowanaTalia=shuffle_deck(talia)
gra4graczy = deal(potasowanaTalia,4)
print(gra4graczy)