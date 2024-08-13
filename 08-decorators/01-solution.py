# Problem 1: Timing function execution , Write a decorator that mesarues the time a functiuon takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}time")
        return result

    return wrapper
@timer
def exampleFunc(n):
    time.sleep(n)

exampleFunc(2)