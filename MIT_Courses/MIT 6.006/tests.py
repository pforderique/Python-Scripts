import unittest
from pip_install import determine_install_order

tests = (
    (
        (
            [[1, 2], [], [1], [1]],
        ),
        3
    ),
    (
        (
            [[1], [2], [0]],
        ),
        None
    ),
    (
        (
            [],
        ),
        0
    ),
    (
        (
            [[] for i in range(10)],
        ),
        1
    ),
    (
        (
            [[i+1] for i in range(100)] + [[0]],
        ),
        None
    ),
    (
        (
            [[]] + [[i//2] for i in range(14)],
        ),
        4
    ),
    (
        (
            [[], [0], [1, 6], [2], [3], [4], [5], [6], [7], [8], [9]],
        ),
        None
    )
)

def check(test):
    args, staff_sol = test
    student_sol = determine_install_order(*args)
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