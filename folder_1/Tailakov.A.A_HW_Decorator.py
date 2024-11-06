#Task 1
# def call_limit(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if wrapper.counter < n:
#                 wrapper.counter += 1
#                 return func(*args, **kwargs)
#             else: # Иначе
#                 raise ValueError("Max calls exceeded")
#         wrapper.counter = 0
#         return wrapper
#     return decorator
#
#
# @call_limit(3)
# def say_hi():
#     print("Hello world!")
#
#
# say_hi()
# say_hi()
# say_hi()
# say_hi()#Будет ошибка т.к лимит вызова = 3

#Task 2
def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, expected_types[i]):
                    raise TypeError(f"Argument at position {i} should be of type {expected_types[i]}")
            for key, value in kwargs.items():
                if not isinstance(value, expected_types[len(args) + list(kwargs.keys()).index(key)]):
                    raise TypeError(f"Argument {key} should be of type {expected_types[len(args) + list(kwargs.keys()).index(key)]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_args(str, str)
def concatenate_strings(s1, s2):
    return s1 + s2

