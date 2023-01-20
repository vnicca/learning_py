'''Exercise 1
There is a set containing the name of the countries. The user needs to be able to:
■ Adding countries;
■ Removing countries;
■ Search countries by entered characters.'''
print('***1 EXCERCISE***')
countries1 = ['Ukraine', 'Poland', 'Germany', 'France', 'Spain', 'Moldova', 'Romania', 'Czech', 'Italy', 'Finland']
print(f'Your countries are: ',countries1)
choice_op1 = str(input("Enter your decision about country: adding(A), deleting(D) or searching(S) : "))
# artists.append('Porcupine Tree')
if choice_op1 == 'A' or choice_op1 == 'a':
    ch_co1 = str(input("Enter name of the country : "))
    countries1.append(ch_co1)
    print(countries1)
elif choice_op1 == 'D' or choice_op1 == 'd':
    ch_co1 = str(input("Enter name of the country : "))
    countries1.remove(ch_co1)
    print(countries1)
elif choice_op1 == 'S' or choice_op1 == 's':
    ch_co1 = str(input("Enter symbols for search : "))
    for i1 in countries1:
        if ch_co1 in i1:
            print(i1, 'yes')
        else:
            print(i1, 'no')


cities1 = ['Rivne', 'Odesa', 'Lutsk', 'Kyiv', 'Lviv', 'Dnipro', 'Kharkiv', 'Yalta', 'Simeiiz', 'Alupka', 'Alushta']
cities2 = ['Rivne', 'Cherkasy', 'Alushta', 'Donetsk', 'Stryi', 'Chop', 'Dubno', 'Odesa', 'Yampil', 'Alushta', 'Khust']
'''Task 2
There are two sets containing names
cities. It is necessary to create a third set containing the names that are in both sets.'''
print('***2 EXCERCISE***')
print(f'Your 1 list is ',cities1)
print(f'Your 1 list is ',cities2)
res1 = [x1 for x1 in cities1 if x1 in cities2]
print(f'Your new list is: ',res1)
'''Task 3
There are two sets containing names
cities. It is necessary to create a third set containing the names that are in the first set, but
not in the second.'''
print('***3 EXCERCISE***')
res3 = [x3 for x3 in cities1 if x3 not in cities2]
print(f'Your new list is: ',res3)

'''Task 4
There are two sets containing names
cities. It is necessary to create a third set containing the names that are in the second set, but
not in the first.'''
print('***4 EXCERCISE***')
res4 = [x4 for x4 in cities2 if x4 not in cities1]
print(f'Your new list is: ',res4)

'''Task 5
There are two sets containing names
cities. You need to create a third set containing unique names for each set.'''
print('***5 EXCERCISE***')
res5 = [x5 for x5 in cities1 + cities2 if x5 not in cities1 or x5 not in cities2]
print(f'Your new list is: ',res5)



'''Task 6
The dictionary stores a set of pairs: Country name ->
Capital. It is necessary to implement functionality for adding, deleting, searching and replacing.'''
print('***6 EXCERCISE***')

countries6 = {'Ukraine': 'Kyiv', 'Poland': 'Warsaw', 'Germany': 'Berlin', 'France': 'Paris', 'Spain': 'Madrid'}
print(f'Your massive is: ',countries6)
choice_op6 = str(input("Enter your decision about country: adding(A), deleting(D), searching(S) or changing(C) : "))
ch_key6 = str(input("Enter country to operate : "))
if choice_op6 == 'A' or choice_op6 == 'a':
    ch_capital6 = str(input("Enter name of the capital : "))
    countries6[ch_key6] = ch_capital6
    print(countries6)
elif choice_op6 == 'D' or choice_op6 == 'd':
    del countries6[ch_key6]
    print(countries6)
elif choice_op6 == 'S' or choice_op6 == 's':
    print(countries6[ch_key6])
elif choice_op6 == 'C' or choice_op6 == 'c':
    ch_new6 = str(input("Enter new value : "))
    countries6[ch_key6] = ch_new6
    print(countries6)