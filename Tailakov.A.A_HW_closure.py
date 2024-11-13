#Task 1
# def repeat_until(f,p):
#     def inner(x):
#         while not p(x):
#             x = f(x)
#         return x
#     return inner
#
# def double(x):
#     return x*2
#
# def greater_than_100(x):
#     return x > 100
#
# double_until_100 = repeat_until(double, greater_than_100)
# result = double_until_100(1)
# print(result)


#Task 2
# def make_counter(n):
#     def counter():
#         nonlocal n
#         if n >= 0:
#             i = n
#             n -= 1
#             return i
#         else:
#             return ""
#     return counter
#
#
#
# count_down = make_counter(4)
# print(count_down())
# print(count_down())
# print(count_down())
# print(count_down())
# print(count_down())
# print(count_down())


#Task 3
# def print_once(func):
#
#     def wrapper(*args, **kwargs):
#         if not wrapper.called:
#             wrapper.called = True
#             return func(*args, **kwargs)
#     wrapper.called = False
#     return wrapper
#
# def hello_world():
#     print("Hello world!")
#
#
# hello_once = print_once(hello_world())
# try:
#     print_once()
#
# except Exception:
#     print("thise function has been applied")
#
# def simulate_growth(months):
#     # Список для хранения клеток разных возрастов
#     # Начинаем с 1 клетки в возрасте 0 месяцев
#     cells = [1]  # На старте у нас есть только 1 клетка в возрасте 0 месяцев
#
#     # Симуляция роста клеток
#     for month in range(1, months + 1):
#         # Для текущего месяца отображаем состояние клеток
#         print(f"Месяц {month}: ", end="")
#
#         # Выводим количество клеток для каждого возраста
#         print(", ".join([f"{cells[i]} клетка(и) ({i}-месячная)" for i in range(len(cells))]), end=" ")
#
#         # Обновляем клетки: сдвигаем их по возрастам
#         cells = [sum(cells[1:])] + cells  # Новые клетки добавляются в начало
#
#         # Выводим общее количество клеток в текущем месяце
#         print(f"→ {sum(cells)} клеток")
#
#
# # Запуск симуляции на 5 месяцев
# simulate_growth(6)


