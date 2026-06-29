import time
from functools import lru_cache
from ai_foundations.utils import timer, memoize

def make_counter():
    count = 0 
    def increment():
        nonlocal count
        count+=1
        return count
    return increment

a = make_counter()
b = make_counter()

print(a())
print(a())
print(a())
print(b())
print(b())

def fib_plain(n):
    if n<2:
        return n
    else:
        return fib_plain(n-1) + fib_plain(n-2)

@lru_cache(maxsize=None)
def fib_cached(n):
    if n<2:
        return n
    else:
        return fib_cached(n-1) + fib_cached(n-2)

fib1 = timer(fib_plain)
fib2 = timer(fib_cached)

@memoize
def fib3(n):
    if n<2:
        return n
    else:
        return fib3(n-1) + fib3(n-2)

fib1(35)
fib2(35)
start = time.perf_counter()
fib3(35)
elapsed = time.perf_counter() - start
print(f"fib3 took {elapsed:.6f}s")



