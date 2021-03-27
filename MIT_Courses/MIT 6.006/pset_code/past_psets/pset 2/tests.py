import unittest
from copyright_match import copyright_match

tests = (
    (
        (
            "Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark",
            "shark",
        ),
        True,
    ),

    (
        (
            "Who ever said money can't solve your problems, Must not have had enough money to solve 'em",
            "Who",
        ),
        True,
    ),

    (
        (
            "VVS my diamonds, I don't need no light to shine Iced out both my wrists, now I can barely see the time",
            "time",
        ),
        True,
    ),

    (
        (
            "There's one hundred and four days of summer vacation And school comes along just to end it",
            "Agent B",
        ),
        False,
    ),

    (
        (
            "Are you cheating on this code submission?",
            "u cheat",
        ),
        True,
    ),

    (
        (
            "sdiovsensriobnskbnseurnflvsuenvlijriodznvbfkurzks",
            "bnseurnflvsu",
        ),
        True,
    ),
    (
        (
            "dnwfgdosnionawiosnvioanviankrnbklsgjvilbnskrvbnklshznkjalhvanjksnksnsuinsleurhglukrngseg",
            "kxbndibfro",
        ),
        False,
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = copyright_match(*args)
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