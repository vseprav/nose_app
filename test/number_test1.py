import time

def one_test():
    print('start test')
    for x in range(0, 10):
        print "We're on time %d" % (x)
    time.sleep(5)
    print('5 seconds')
    for x in range(0, 10):
        print "We're on time %d" % (x)

    assert 1

def two_test():
    print('start test')
    for x in range(0, 10):
        print "We're on time %d" % (x)
    time.sleep(5)
    print('5 seconds')
    for x in range(0, 10):
        print "We're on time %d" % (x)

    assert 1


def three_test():
    print('start test')
    for x in range(0, 10):
        print "We're on time %d" % (x)
    time.sleep(5)
    print('5 seconds')
    for x in range(0, 10):
        print "We're on time %d" % (x)

    assert 1