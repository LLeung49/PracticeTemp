import unittest
from ArrayString import isUnique, one_way, rotate_matrix


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


class RotateMatrixTest(unittest.TestCase):
    def test(self):
        a = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        b = [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]
        self.assertEqual(rotate_matrix(a), b)

    def test1(self):
        b = [[7, 4, 1],
             [8, 5, 2]
             ]
        self.assertEqual(rotate_matrix(b), False)

    def test2(self):
        a = [[1, 2, 3, 'a'],
             [4, 5, 6, 'b'],
             [7, 8, 9, 'c'],
             ['a', 'b', 'c', 'd']]
        b = [['a', 7, 4, 1],
             ['b', 8, 5, 2],
             ['c', 9, 6, 3],
             ['d', 'c', 'b', 'a']]
        self.assertEqual(rotate_matrix(a), b)

# if __name__ =='__main__':
#     # is_unique.test()
#     # one_way_test.test()
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(RotateMatrixTest)
unittest.TextTestRunner(verbosity=2).run(suite)
