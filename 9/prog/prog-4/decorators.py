def count(f):
    called = 0

    def wrapped(*args, **kwargs):
        nonlocal called
        called += 1
        return f(*args, **kwargs), called

    return wrapped


# @override


def benchmark(iters=1):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for _ in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print("[*] Среднее время выполнения: {} секунд.".format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


def time_count(f):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        return res, end_time - start_time

    return wrapper


def squared(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res * res

    return wrapper


@time_count
@count
# @benchmark(iters=5)
def hello(name: str) -> str:
    return f"Hello, {name}"


@count
def abc():
    return "abc"


@squared
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


@squared
def fact_iter(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


print(hello("admin"))
print(hello(""))
print(hello(""))
print(fact(3))
print(fact_iter(3))
