from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()

a = 0
b = 0

s = 0


def access_a():
    global a

    lock1.acquire()

    a += 1

    lock1.release()


def access_b():
    global b
    lock2.acquire()

    b += 1

    lock2.release()


def func1():
    global s
    access_a()
    for _ in range(100000000):
        s += 1
    access_b()
    print(s)


def func2():
    global s
    access_b()
    for _ in range(100000000):
        s += 1
    access_a()
    print(s)


t1 = Thread(target=func1, daemon=False)
for _ in range(1000000):
    s += 1
print(s)
t2 = Thread(target=func2, daemon=False)

print("Threads started")
t1.start()
t2.start()

t1.join()
t2.join()
