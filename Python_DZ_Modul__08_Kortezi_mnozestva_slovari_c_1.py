'''Exercise 1
There are three tuples of integers to be found
elements that are in all tuples.'''
print('***FIRST EXCERCISE***')
import random
length = 10
AA = []
BB = []
CC = []
l1 = random.randint(-10, 10)
l2 = random.randint(-10, 10)
l3 = random.randint(-10, 10)
for i in range(length):
    a = random.randint(-20, 100)
    b = random.randint(-20, 100)
    c = random.randint(-20, 100)
    AA.append(a)
    BB.append(b)
    CC.append(c)
print(f'Your numbers are: \nfirst tuple: {AA}\nsecond tuple: {BB}\nthird tuple: {CC}')
ALL_Cor = AA + BB + CC
print(f'All numbers: {ALL_Cor}')

counter = {}

for elem in ALL_Cor:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(f'These numbers are duplicated: {doubles}')

'''Task 2
There are three tuples of integers to be found
elements that are unique to each list.'''
print('***SECOND EXCERCISE***')
import random

import collections
new = 0
length1 = 10
AA2 = []
BB2 = []
CC2 = []
for i2 in range(length1):
    a2 = random.randint(-10, 10)
    b2 = random.randint(-10, 100)
    c2 = random.randint(-10, 10)
    AA2.append(a2)
    BB2.append(b2)
    CC2.append(c2)
print(f'Your numbers are: \nfirst tuple: {AA2}\nsecond tuple: {BB2}\nthird tuple: {CC2}')

AA2_new = tuple(set(AA2))

BB2_new = tuple(set(BB2))

CC2_new = tuple(set(CC2))
print(f'Your new tuples without duplicates: \nfirst tuple: {AA2_new}\nsecond tuple: {BB2_new}\nthird tuple: {CC2_new}')

'''Task 3
There are three tuples of integers to find elements,
which are in each of the tuples and are
in each of the tuples at the same position'''
print('***THIRD EXCERCISE***')
import random

import collections

length2 = 10
AA3 = []
BB3 = []
CC3 = []
for i3 in range(length2):
    a3 = random.randint(0, 2)
    b3 = random.randint(0, 2)
    c3 = random.randint(0, 2)
    AA3.append(a3)
    BB3.append(b3)
    CC3.append(c3)
print(f'Your numbers are: \n1 tuple: {AA3}\n2 tuple: {BB3}\n3 tuple: {CC3}')
new_numbers = list()
index_numbers = list()
for i3_1, elem3_1 in enumerate(AA3):
    for i3_2, elem3_2 in enumerate(BB3):
        for i3_3, elem3_3 in enumerate(CC3):
            if i3_1 == i3_2 == i3_3 and elem3_1 == elem3_2 == elem3_3:
                new_numbers.append(elem3_1)
                index_numbers.append(i3_1)

if new_numbers == []:
    print('No identical numbers')
elif new_numbers != []:
    print(f'Your numbers are {new_numbers} in position {index_numbers} in each of the tuples')
else:
    print('Error! Something went wrong!')
