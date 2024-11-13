#Task 1
# def sum(n):
#     if n < 9:
#         return n
#     else:
#         return n % 10 + sum(n // 10)
#
# def isLucky(n):
#     if n < 100000:
#         return False
#     else:
#         return sum(n % 1000) == sum(n // 1000)
#
# print(isLucky(123420))
# print(isLucky(723422))

#Task 2
# import random
#
#
# def order_matrix(matrix):
#     for i in range(len(matrix)):
#         if i % 2 == 0:  # для четных строк
#             matrix[i].sort()  # сортируем по возрастанию
#         else:  # для нечетных строк
#             matrix[i].sort(reverse=True)  # сортируем по убыванию
#     return matrix
#
# matrix = [[random.randint(1,10) for i in range(5)] for j in range(5)]
# print(matrix)
#
# from random import randint
# def gen_matrix():
#         height = randint(2, 5)
#         width = randint(2, 5)
#         a = []
#         gen = 1
#         for i in range(height):
#             a.append([])
#             for j in range(width):
#                 a[i].append(randint(0, 4))
#                 gen *= a[i][j]
#             print(*map('{:>3d}'.format, a[i]))
#         return gen
# print(gen_matrix())


#task 1
# import random
# width = int(input('Enter the width of matrix: '))
# hight = int(input('Enter the hight of matrix: '))
# matrix = [[random.randint(1,10) for i in range(width)] for i in range(hight)]
# for i in matrix:
#     for j in i:
#         print(j, end='\t')
#     print()
#
# def min_diag_element(matrix):
#     diag_elements = []
#     for i in range(width):
#         for j in range(hight):
#             if i == j:
#                 diag_elements.append(matrix[i][j])
#                 return min(diag_elements)


#print(min_diag_element(matrix))

#task 2
# def get_work_day(month):
#     my_matrix = [[month[i][j] for j in range(5) if month[i][j] != 0] for i in range(len(month))]
#     return my_matrix
#
# month_zero = [[0 for _ in range(7)] for _ in range(5)]
# day = 1
# for row in month_zero:
#     for d in range(len(row)):
#         if day <= 31:
#             row[d] = day
#             day += 1
#     [print(*row, sep='\t') for row in month_zero]
# print('*' * 27)
# work_day_list = get_work_day(month_zero)
# [print(*row, sep='\t') for row in work_day_list]

#task 3
# number = int(input("enter the number"))
# symbol = input("enter the symbol")
# def out_symbols(number, symbol):
#     c = number * symbol
#     print(c)
#
#
# out_symbols(number,symbol)
# out_symbols(20,"-")

#task 4
# def is_eval(num: int, flag: bool = True) -> int:
#     count = sum([int(i) for i in str(num)
#                  if int(i) % 2 != flag])
#     return count

#рекурсии!
#task 5
# def range(n):
#     print(n)
#     if n == 0:
#         return
#     range(n-1)
#
# print(range(10))

#task 6
# def degree(number, exp):
#     if (exp == 1):
#         return (number)
#     if (exp != 1):
#         return (number * degree(number, exp - 1))
#
#
# number = int(input("Enter the number: "))
# exp = int(input("Enter the number power: "))
# print("Result: ", degree(number, exp))

#Task 7
# def summ(a, b):
#     if b == a:
#         return b
#     return b + summ(a, b - 1)
#
#
# number1 = int(input("Enter the lowest number: "))
# number2 = int(input("Enter the highest number: "))
# print(summ(number1, number2))

#task 8
# import random
# def find_sequence(lst):
#     min_sum = float('inf')
#     start_pos = -1
#     for i in range(len(lst) - 9):
#         current_sum = 0
#         for j in range(i, i + 10):
#             current_sum += lst[j]
#         if current_sum < min_sum:
#             min_sum = current_sum
#             start_pos = i
#     return start_pos
#
# lst = [random.randint(0, 100) for _ in range(30)]
# print(lst)
# print(find_sequence(lst))



# import random
# def min_sum(nums=None, i=0, final_sum=0, index=0):
#     if nums is None:
#         nums = [random.randint(1, 30) for i in range(100)]
#         current_min = sum([nums[i] for i in range(i, i+10)])
#         if final_sum > current_min or final_sum == 0:
#             final_sum = current_min
#             index = i
#     try:
#         return min_sum(nums, i + 1, final_sum, index)
#     except IndexError:
#         for i in range(len(nums)):
#             if index <= i < index + 10:
#                 print('\033[32m', end='')
#             else:
#                 print('\033[0m', end='')
#                 print(nums[i], end=' ')
#                 print()
#             return final_sum,index
#
# print(min_sum())

#Example 1
# def summa (a,b):
#     def check_ab(a,b):
#         return a > 0 and b > 0
#
#     if check_ab(a,b):
#         return a + b
#     return "Wrong input"
#
#
# print(summa(2, 2))

#lambda

#add = lambda x: x + 1

# lst = [[1,1],[2,2]]
# print(list(map(lambda x: x[0]**2, lst)))


# lst = [1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x: x % 2 == 0, lst)))

# even_list = lambda x: [i for i in x if i % 2 == 0]
# print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# strings_list = ["asd",'ddd','sad','rrr']
# get_strings_with_a = lambda strings_list: [word for word in strings_list if 'a' in word]
# print(get_strings_with_a(strings_list))

#Замыкания
# def func1(sym):
#
#     def func2(word):
#
#         return sym + word + sym
#
#     return func2
#
# name1 = func1('*')
# name2 = func1('#')
# print(name1("name1"))
# print(name2("name2"))

#Counter
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     return inner
# # Пример использования
# c = counter()
# c() # 1
# c() # 1
# c() # 1

# def Password_protection(password):
#     def closure(entered_password):
#         if entered_password == password:
#             return sensitive_function()
#         else:
#             return "Error: Incorrect Password"
#     return closure
# # Пример использования
# def sensitive_function():
#     return "Hello, World!"
# protected_function = Password_protection("MyPassword")
# print(protected_function("WrongPassword")) # Output: Error: Incorrect Password
# print(protected_function("MyPassword")) # Output: Hello, World!

# def memoize(func):
#     cache = {}
#     def memoized_func(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             result = func(*args)
#             cache[args] = result
#             return result
#     return memoized_func

# import time
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f" Lead function time {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper
# @measure_time
# #Create a random list
# def create_random_list(n):
#     import random
#     return [random.randint(-100000, 100000) for _ in range(100000)]
# create_random_list(10000)

# def cache_fibo(func):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         if args not in cache:
#             cache[args] = func(*args, **kwargs)
#         return cache[args]
#     return wrapper
# @cache_fibo
# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

