import time


def func_decorator1(f):
    def wrapper():
        print("-" * 15)
        f()
        print("-" * 15)
    return wrapper

def func_decorator2(f):
    def wrapper():
        print("*" * 15)
        f()
        print("*" * 15)
    return wrapper

@func_decorator2
@func_decorator1
def demo_function():
    print("Hello")


def sum_decorator(f):
    def wrapper(*args, **kwargs):
        value = f(*args, **kwargs)
        print("The sum is : ")
        return value
    return wrapper

@sum_decorator
def sum_num(a, b):
    return a+b

def served_by(server):
    def wrapper(f):
        def num_wrapper(n):
            return f(n) + f", dear {server}!"
        return  num_wrapper
    return  wrapper

def thank_you(f):
    def wrapper(n):
        return f"{f(n)} Thank you so much!"
    return  wrapper

@thank_you
@served_by("sir")
def eggs(n):
    return f"I would like to order {n} eggs"


def decorated_goodbye(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) + "Have a nice day!"
    return  wrapper

def named_spam(name):
    def decorated_spam(f):
        def num_wrapper(n):
            return f"I am {name} and " + f(n) + "\n"
        return num_wrapper
    return  decorated_spam

@decorated_goodbye
@named_spam("alien")
def spam(n):
    formatted_spam="spam, " * (n - 1) + "spam"
    return f"I would like to {formatted_spam}."

def fib_memoizer(f):
    fib_values={}

    def wrapper(n):
        if n in fib_values:
            return fib_values[n]

        current_value=f(n)
        fib_values[n]= current_value
        return current_value
    return wrapper

@fib_memoizer
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

@fib_memoizer
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def execution_time_decorator(f):
    def wrapper(*args, **kwargs):
        print(f"Function {f.__name__} with agrs : {args} and kwargs : {kwargs} starts execution")
        star_time = time.perf_counter()
        res = f(*args, **kwargs)
        end_time= time.perf_counter()
        print(f"Function {f.__name__} took {end_time-star_time} seconds to execute")
        return res
    return wrapper

@execution_time_decorator
def sum_nums1(n):
    return n*(n+1)//2

@execution_time_decorator
def sum_nums2(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res
