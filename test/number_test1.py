import time
import sys

def test_1():
    print('start test_1')
    for x in range(0, 200):
        print "We're on time %d" % (x)

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 200):
        print "We're on time %d" % (x)

    assert 1
    sys.stdout.flush()

def test_2():
    print('start test_2')
    for x in range(0, 200):
        print "We're on time %d" % (x)

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 200):
        print "We're on time %d" % (x)

    assert 1
    sys.stdout.flush()

def test_3():
    print('start test_3')
    for x in range(0, 200):
        print "We're on time %d" % (x)

    sys.stdout.flush()
    time.sleep(10)

    for x in range(0, 200):
        print "We're on time %d" % (x)

    assert 1
    sys.stdout.flush()