import time
import sys

def test_1():
    time.sleep(100)
    print('start test_1')
    for x in range(0, 50):
        print("We're on time %d" % (x))

    sys.stdout.flush()