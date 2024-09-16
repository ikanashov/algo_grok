# Classic CS Problems in Python
from functools import lru_cache
from typing import Generator


def fib1(n: int) -> int:  # does not work because of infinitive recursion
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2:  # base case (will return if n 0 or 1) without recursion
        return n
    return fib2(n - 1) + fib2(n - 2)


memo: dict[int, int] = {0: 0, 1: 1}  # our base cases


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # base case (will return if n 0 or 1) without recursion
        return n
    return fib4(n - 1) + fib4(n - 2)


def fib5(n: int) -> int:
    if n == 0:
        return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1   # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    print(fib2(10))  # if bigger then never end because not used memoization
    print(fib3(200))
    print(fib4(200))
    print(fib5(200))
    print(list(fib6(5)))
