from multiprocessing import Process
from threading import Thread
import time

# n = int(input())


def hello(*args):
    s = 0
    for _ in range(1000000):
        s += 1
    print(f"hello {args[0]} {s}")


n = 6

threads = [Thread(target=hello, args=(i,), daemon=False) for i in range(n)]

for i in range(n):
    threads[i].start()

for i in range(n):
    threads[i].join()
