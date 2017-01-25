import time
import sys

def test_1():
    time.sleep(10)
    print('start test_1')
    for x in range(0, 2000):
        print("We're on time %d" % (x))

    sys.stdout.flush()

def test_2():
    time.sleep(30)
    print('start test_2')
    for x in range(0, 20000):
        print("We're on time %d" % (x))

    sys.stdout.flush()

def test_3():
    time.sleep(30)
    print('start test_3')
    for x in range(0, 20000):
        print("We're on time %d" % (x))

    sys.stdout.flush()
def test_4():
    time.sleep(30)
    print('start test_4')
    for x in range(0, 20000):
        print("We're on time %d" % (x))

    sys.stdout.flush()

def test_5():
    time.sleep(30)
    print('start test_5')
    for x in range(0, 20000):
        print("We're on time %d" % (x))

    sys.stdout.flush()