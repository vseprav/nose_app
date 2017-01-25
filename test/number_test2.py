import time
import sys

def test_1():
    print('start test_1')
    for x in range(0, 2000):
        print("We're on time %d" % (x))
    time.sleep(100)
    sys.stdout.flush()