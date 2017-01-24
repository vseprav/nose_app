import time

def test_1():
    assert 1
    print('start test_1')
    for x in range(0, 1000):
        print "We're on time %d" % (x)

    assert 2
    time.sleep(10)

def test_2():
    print('start test_2')
    for x in range(0, 1000):
        print "We're on time %d" % (x)

    assert 2
    time.sleep(10)

def test_3():
    print('start test_3')
    for x in range(0, 1000):
        print "We're on time %d" % (x)

    assert 1+2
    time.sleep(10)