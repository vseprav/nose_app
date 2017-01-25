import time
import sys

def test_1():
    time.sleep(10)
    print('start test_1')
    for x in range(0, 2000):
        print("We're on time %d" % (x))

    sys.stdout.flush()