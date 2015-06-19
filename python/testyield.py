def is_even(n):
    if n == 1:
        return False
    else:
        return n % 2 == 0


def even_numbers(n = 1):
    for i in range(1, n+1):
        if is_even(i):
            yield i

for x in even_numbers(50):
    print x

