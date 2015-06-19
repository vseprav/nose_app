import unittest
import myunit.app

class MyUnitTest(unittest.TestCase):

  @staticmethod
  def setUp():
    print 4+"3"

  def testInit(self):
    app = myunit.app.App(100)
    self.assertEquals(app.var, 100)

  def testGetVar(self):
    app = myunit.app.App(200)
    self.assertEquals(app.get_var(), 200)
