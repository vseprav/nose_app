import time
import sys

def test_1():
    print('start test_1')
    for x in range(0, 2000000):
        print("We're on time %d" % (x))

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 2000000):
        print("We're on time %d" % (x))

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 2000000):
        print("We're on time %d" % (x))

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 2000000):
        print("We're on time %d" % (x))

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 2000000):
        print("We're on time %d" % (x))

    sys.stdout.flush()