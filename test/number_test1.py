import time

def test_1():
    print('start test')
    for x in range(0, 1000):
        print "We're on time %d" % (x)

    time.sleep(5)

    for x in range(0, 1000):
        print "We're on time %d" % (x)

    time.sleep(30)

def test_2():
    print('start test')
    for x in range(0, 1000):
        print "We're on time %d" % (x)

    time.sleep(5)

    for x in range(0, 1000):
        print "We're on time %d" % (x)

    time.sleep(30)