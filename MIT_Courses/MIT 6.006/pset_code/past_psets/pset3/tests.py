import unittest
from construct_preorder_traversal import construct_preorder_traversal
# from newalgo import construct_preorder_traversal

tests = (
    (
        (
            ["a"],
            ["a"]
        ),
        ["a"]
    ),
    (
        (
            ["a", "b", "c", "d", "e", "f", "g"],
            ["a", "c", "b", "e", "g", "f", "d"]
        ),
        ["d", "b", "a", "c", "f", "e", "g"]
    ),
    (
        (
            ['d', 'b', 'a', 'e', 'c', 'f'],
            ['d', 'b', 'e', 'f', 'c', 'a']
        ),
        ['a', 'b', 'd', 'c', 'e', 'f']
    ),
    (
        (
            ['h', 'd', 'i', 'b', 'j', 'e', 'k', 'a', 'f', 'g', 'c'],
            ['h', 'i', 'd', 'j', 'k', 'e', 'b', 'g', 'f', 'c', 'a']
        ),
        ['a', 'b', 'd', 'h', 'i', 'e', 'j', 'k', 'c', 'f', 'g']
    ),
    (
        (
            ['h', 'd', 'b', 'a'],
            ['h', 'd', 'b', 'a']
        ),
        ['a', 'b', 'd', 'h']
    ),
    (
        (
            ['b', 'a', 'c', 'd', 'e'],
            ['b', 'e', 'd', 'c', 'a']
        ),
        ['a', 'b', 'c', 'd', 'e']
    ),
    (
        (
            ['b', 'c', 'd', 'e', 'f', 'a', 'j', 'i', 'h', 'g'],
            ['f', 'e', 'd', 'c', 'b', 'j', 'i', 'h', 'g', 'a']
        ),
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = construct_preorder_traversal(*args)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))

    def test_06(self):
        self.assertTrue(check(tests[5]))

    def test_07(self):
        self.assertTrue(check(tests[6]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)