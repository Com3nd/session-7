from typing import Optional


def minus_one(n: int) -> Optional[int]:
    if n == 0:
        print("Blast off!")
        return
    print(n)
    return minus_one(n - 1)


def add_natural_numbers(n) -> int:
    if n == 1:
        return 1
    return n + add_natural_numbers(n - 1)


print(add_natural_numbers(10))
