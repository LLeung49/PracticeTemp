import unittest
from PyUnittest import plus


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(plus(3, 5), 8)

    def test1(self):
        self.assertEqual(plus(3, 4), 8)

if __name__ =='__main__':
    MyTest.test()
    assert plus(5,3) == 8
