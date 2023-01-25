'''Exercise 1
Write a function that calculates the product
elements of a list of integers. The list is passed as a parameter. The result is returned from the function.'''
print('***1 Task***')


def mult_l1(l1):
    res_1 = 1
    for x in l1:
        res_1 = res_1 * x
    return res_1


l1 = [45, 56, 1, 133, 17, 11, 5, 10, -2, 9]

print(mult_l1(l1))
'''Task 2
Write a function to find the minimum in
list of integers. The list is passed as a parameter.
The result is returned from the function.'''
print('***2 Task***')


def mini_el_2(l2):
    min_el = min(l2)
    l2.pop(l2.index(min_el))
    print("Minimal element is:", min_el)


l2 = [0, 45, -123, 78, 456, 74, -2, 12, 78, 10, -789]
Minimal = mini_el_2(l2)
'''Task 3
Write a function that determines the number of primes in a list of integers. The list is passed as
parameter. The result is returned from the function.'''
print('***3 Task***')


def prime_num(n):
    if n < 1:
        return False
    for i in range(2, 1 + n // 2):
        if (n % i) == 0:
            return False

    return True


def prime_num_count(list_3):
    count = 0
    for i in list_3:
        count = count + 1 if prime_num(i) else count
    return count


list_3 = [17, 23, 63, 7, 11, 78, 99, 60, 45]  # 5 простих чисел
print('Count of primes is: ', prime_num_count(list_3))
'''Task 4
Write a function to remove integers from a list
some given number. Return from function
the number of items removed.'''
print('***4 Task***')


def remov_4(l4):
    print("List before delete")
    print(l4)
    l4.remove(8)
    print("List after delete")
    print(l4)
    count_rem = 0
    count_rem += 1
    print('Number of deleted items :')
    return count_rem


l4 = [30, 5, 2, 7, 56, 71, 22, 1, 8, 11]
i4 = [8]
print(remov_4(l4))
'''Task 5
Write a function that gets two lists in
as a parameter and returns a list containing
elements of both lists.'''
print('***5 Task***')


def together_5():
    tog_5 = l5_1 + l5_2
    print(tog_5)


l5_1 = [1, 3, 78, 7, 0]
l5_2 = [13, 45, 17, 26, 1001]
print('Your 1 list :', l5_1)
print('Your 2 list :', l5_2)
print('Your NEW list :')
print(together_5())
'''Task 6
Write a function that calculates the degree of each
an element of a list of integers. The value for the degree is passed
as a parameter, the list is also passed as
parameter. The function returns a new list containing the results.'''
print('***6 Task***')

l6 = [1, 8, 12, 5, 63, 86, 10, 9, 5, 230]
l_d6 = [6, 2, 0, -10, 2, 6, 1, 3, 4, 10]


def degree_turning(l6, l_d6):
    result_6 = []
    for i1, i2 in zip(l6, l_d6):
        result_6.append(i1**i2)
        print("The product of 2 lists is: ", result_6)


print(degree_turning(l6, l_d6))
