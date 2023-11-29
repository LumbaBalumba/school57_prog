from threading import Thread, Lock

a = 1

lock = Lock()


def func1():
    global a
    lock.acquire()
    for _ in range(1000000):
        pass
    a += 1
    lock.release()


def func2():
    for _ in range(1000000):
        pass
    global a
    lock.acquire()
    a *= 3
    lock.release()


t1 = Thread(target=func1, args=(), daemon=False)
t2 = Thread(target=func2, args=(), daemon=False)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)
