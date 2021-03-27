import unittest
from solve_noolbs import solve_noolbs

tests = (
    (
        (
            ((1, 1, 0), (0, 0, 0), (0, "x", 0)),
        ),
        None
    ),
    (
        (
            ((1, 0, 0), (0, 0, 0), (0, "x", 0)),
        ),
        2
    ),
    (
        (
            (
                (1, 1, 0, 0),
                (1, 0, 0, 2),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, "x", 0)
            ),
        ),
        13
    ),
    (
        (
            (
                (0, 1, 2, 1),
                (1, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, "x", 0),
            ),
        ),
        12
    ),
    (
        (
            (
                (1, 2, 1, 1),
                (1, 0, 1, 2),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, "x", 0),
            ),
        ),
        None
    ),
    (
        (
            (
                (2, 1, 1, 0),
                (3, 2, 1, 0),
                (0, 0, 2, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, "x", 0),
            ),
        ),
        16
    ),
    (
        (
            (
                (1, 2, 3, 3),
                (1, 3, 3, 2),
                (0, 0, 0, 0),
                (0, 3, 1, 1),
                (0, 2, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, "x", 0),
            ),
        ),
        None
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = solve_noolbs(*args)
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


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)