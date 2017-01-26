import unittest
from ArrayString import isUnique, one_way


class is_unique(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isUnique('dfs'), True)

    def test_2(self):
        self.assertEqual(isUnique('sfefwef'), False)

class one_way_test(unittest.TestCase):

    def test(self):
        self.assertEqual(one_way('dfs','dgs'), True)

    def test1(self):
        self.assertEqual(one_way('sfefwef','gsfg'), False)

    def test2(self):
        self.assertEqual(one_way('pale', 'ple'), True)

    def test3(self):
        self.assertEqual(one_way('pales', 'pale'), True)

    def test4(self):
        self.assertEqual(one_way('pale', 'bale'), True)

    def test5(self):
        self.assertEqual(one_way('pale', 'bake'), False)

# if __name__ =='__main__':
#     # is_unique.test()
#     # one_way_test.test()
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(one_way_test)
unittest.TextTestRunner(verbosity=2).run(suite)
