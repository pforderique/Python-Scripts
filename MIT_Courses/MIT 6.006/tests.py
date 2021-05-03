import unittest
from find_start_times import find_start_times


def check(constraints, solution, valid, verbose=True):
    """Checks if a given solution is correct for a list of constraints.

    Args:
        constraints: A list of constraints.
        solution: A dictionary with start time assignments.
        valid: Should solution not be None?
    
    Returns:
        If the given solution is valid for the constraints.
    """

    if not valid:
        if solution is not None:
            if verbose:
                print(
                    "Your solution produced an output even though problem was impossible."
                )
            return False
        return True

    # Check each constraint.
    for a, b, t in constraints:
        if a not in solution or b not in solution:
            if verbose:
                print("Your output did not contain all variables.")
            return False

        satisfies = solution[a] - solution[b] <= t

        if not satisfies:
            if verbose:
                print(
                    "Your output does not satisfy condition",
                    (a, b, t),
                    f"You assigned {a}={solution[a]} and {b}={solution[b]}.",
                )
            return False

    return True


tests = [
    (
        [
            ("s2", "s1", -4),
            ("s3", "s1", -15),
            ("s1", "s4", 7),
            ("s4", "s3", 10),
            ("s3", "s2", -8),
        ],
        True,
    ),
    ([("s1", "s2", 7), ("s2", "s3", -2), ("s3", "s4", -10), ("s4", "s1", 3),], False,),
]

tests += [
    (
        [
            ("s4", "s2", 7),
            ("s2", "s7", 7),
            ("s6", "s2", 10),
            ("s7", "s6", 9),
            ("s4", "s8", -1),
            ("s0", "s9", 3),
            ("s2", "s9", -10),
        ],
        True,
    ),
    (
        [
            ("s3", "s0", -7),
            ("s1", "s0", 3),
            ("s5", "s1", 5),
            ("s0", "s2", 2),
            ("s1", "s3", -3),
            ("s2", "s4", 9),
            ("s5", "s4", -8),
            ("s5", "s6", -4),
            ("s0", "s6", -1),
            ("s9", "s8", -4),
        ],
        True,
    ),
    (
        [
            ("s0", "s38", 5),
            ("s0", "s13", 10),
            ("s9", "s0", 6),
            ("s16", "s1", -3),
            ("s35", "s2", 3),
            ("s14", "s2", 0),
            ("s19", "s2", -6),
            ("s22", "s2", 1),
            ("s13", "s2", -10),
            ("s47", "s2", 6),
            ("s9", "s2", 0),
            ("s3", "s47", 9),
            ("s3", "s26", 6),
            ("s11", "s3", -6),
            ("s6", "s3", 7),
            ("s30", "s3", 9),
            ("s32", "s3", 3),
            ("s40", "s4", 8),
            ("s19", "s4", -1),
            ("s4", "s7", 10),
            ("s11", "s5", 9),
            ("s20", "s5", 9),
            ("s31", "s6", 4),
            ("s39", "s7", 2),
            ("s43", "s7", 9),
            ("s7", "s0", 6),
            ("s5", "s7", -8),
            ("s15", "s7", 7),
            ("s30", "s7", 8),
            ("s48", "s7", 5),
            ("s21", "s7", 0),
            ("s7", "s26", 6),
            ("s15", "s8", 5),
            ("s8", "s26", 3),
            ("s8", "s3", 4),
            ("s21", "s8", 5),
            ("s3", "s9", 0),
            ("s9", "s8", -1),
            ("s41", "s9", 0),
            ("s9", "s33", 8),
            ("s37", "s9", 3),
            ("s47", "s9", 6),
            ("s13", "s9", 6),
            ("s9", "s39", 8),
            ("s38", "s9", 4),
            ("s31", "s9", 4),
            ("s44", "s10", -7),
            ("s46", "s10", 0),
            ("s14", "s10", -4),
            ("s9", "s10", 1),
            ("s4", "s10", 2),
            ("s30", "s10", -1),
            ("s10", "s36", 6),
            ("s11", "s12", 0),
            ("s7", "s12", 4),
            ("s18", "s12", 2),
            ("s12", "s21", 2),
            ("s35", "s12", 6),
            ("s12", "s22", 8),
            ("s12", "s3", 7),
            ("s34", "s13", 5),
            ("s3", "s13", 7),
            ("s16", "s13", 9),
            ("s43", "s13", -6),
            ("s13", "s33", -1),
            ("s8", "s13", 10),
            ("s8", "s14", 10),
            ("s25", "s14", 8),
            ("s14", "s31", -4),
            ("s7", "s14", 10),
            ("s22", "s15", 9),
            ("s47", "s15", 2),
            ("s33", "s15", -4),
            ("s19", "s15", 6),
            ("s25", "s15", 2),
            ("s5", "s15", -9),
            ("s34", "s15", -10),
            ("s48", "s15", 8),
            ("s17", "s15", 2),
            ("s6", "s16", 5),
            ("s21", "s16", 9),
            ("s39", "s16", 9),
            ("s16", "s14", 2),
            ("s29", "s17", 5),
            ("s9", "s17", 2),
            ("s11", "s17", -4),
            ("s20", "s17", 9),
            ("s22", "s18", -1),
            ("s34", "s18", 7),
            ("s28", "s18", 8),
            ("s39", "s18", -2),
            ("s35", "s18", 4),
            ("s30", "s21", 9),
            ("s27", "s21", -2),
            ("s26", "s21", 5),
            ("s21", "s31", 0),
            ("s6", "s22", 7),
            ("s22", "s23", 1),
            ("s11", "s22", -2),
            ("s36", "s22", 7),
            ("s41", "s22", 2),
            ("s25", "s22", 9),
            ("s11", "s23", 1),
            ("s6", "s23", 3),
            ("s23", "s46", 4),
            ("s36", "s23", 3),
            ("s2", "s23", -2),
            ("s45", "s23", 9),
            ("s16", "s24", -7),
            ("s6", "s24", 5),
            ("s22", "s24", 5),
            ("s32", "s24", 5),
            ("s21", "s24", 8),
            ("s36", "s24", 5),
            ("s11", "s24", 1),
            ("s37", "s24", 6),
            ("s44", "s24", 10),
            ("s49", "s24", 9),
            ("s21", "s25", -6),
            ("s25", "s9", 8),
            ("s20", "s25", -7),
            ("s26", "s46", 9),
            ("s26", "s39", 10),
            ("s31", "s26", 0),
            ("s22", "s26", 10),
            ("s26", "s44", 2),
            ("s29", "s26", 9),
            ("s6", "s29", 10),
            ("s29", "s16", 3),
            ("s39", "s29", -4),
            ("s29", "s35", 6),
            ("s0", "s29", 2),
            ("s1", "s29", 10),
            ("s5", "s29", 3),
            ("s30", "s4", 2),
            ("s15", "s30", 8),
            ("s20", "s30", -4),
            ("s6", "s30", -10),
            ("s8", "s30", 10),
            ("s22", "s30", 5),
            ("s7", "s31", 7),
            ("s31", "s10", 5),
            ("s32", "s31", -4),
            ("s16", "s31", 2),
            ("s36", "s31", 8),
            ("s44", "s31", 9),
            ("s31", "s40", 5),
            ("s27", "s31", 8),
            ("s11", "s32", 4),
            ("s33", "s30", 1),
            ("s41", "s33", 10),
            ("s33", "s8", 10),
            ("s44", "s33", 9),
            ("s27", "s33", 5),
            ("s31", "s34", 9),
            ("s35", "s9", 10),
            ("s14", "s35", 10),
            ("s28", "s35", 10),
            ("s44", "s35", 7),
            ("s16", "s35", 1),
            ("s4", "s36", 3),
            ("s12", "s36", 7),
            ("s18", "s36", 4),
            ("s36", "s37", 6),
            ("s3", "s36", 4),
            ("s37", "s48", 4),
            ("s28", "s37", -8),
            ("s14", "s37", -6),
            ("s6", "s37", 8),
            ("s32", "s38", -5),
            ("s24", "s38", -3),
            ("s20", "s38", 3),
            ("s36", "s38", -1),
            ("s38", "s49", 5),
            ("s15", "s39", 6),
            ("s39", "s48", 3),
            ("s3", "s39", 10),
            ("s39", "s11", 3),
            ("s39", "s25", 3),
            ("s32", "s40", 6),
            ("s40", "s12", 2),
            ("s11", "s41", -3),
            ("s41", "s47", 3),
            ("s43", "s41", 1),
            ("s1", "s41", 6),
            ("s21", "s42", 7),
            ("s29", "s42", 5),
            ("s6", "s42", 9),
            ("s44", "s42", -1),
            ("s48", "s42", 7),
            ("s36", "s42", -1),
            ("s20", "s43", 10),
            ("s5", "s43", 7),
            ("s40", "s44", -4),
            ("s44", "s39", 8),
            ("s25", "s45", -4),
            ("s35", "s45", -2),
            ("s42", "s45", 7),
            ("s18", "s45", 4),
            ("s10", "s45", 8),
            ("s49", "s45", -2),
            ("s29", "s46", 1),
            ("s46", "s0", 10),
            ("s11", "s46", 5),
            ("s8", "s46", 5),
            ("s46", "s9", 5),
            ("s42", "s46", 0),
            ("s14", "s46", -7),
            ("s28", "s46", 3),
            ("s19", "s46", -3),
            ("s22", "s47", 4),
            ("s47", "s12", 6),
            ("s47", "s29", 6),
            ("s39", "s47", 9),
            ("s16", "s47", -2),
            ("s38", "s48", 10),
            ("s27", "s48", -5),
            ("s47", "s48", 4),
            ("s22", "s48", 5),
            ("s48", "s41", -1),
            ("s31", "s48", -1),
            ("s48", "s29", 8),
            ("s1", "s48", 8),
            ("s14", "s49", -5),
            ("s41", "s49", -4),
            ("s40", "s49", 1),
            ("s5", "s49", 0),
            ("s49", "s7", 7),
            ("s6", "s49", 6),
            ("s43", "s49", 3),
        ],
        True,
    ),
]


class TestCases(unittest.TestCase):
    def test_01(self):
        C, V = tests[0]
        solution = find_start_times(C)
        self.assertTrue(check(C, solution, V))

    def test_02(self):
        C, V = tests[1]
        solution = find_start_times(C)
        self.assertTrue(check(C, solution, V))

    def test_03(self):
        C, V = tests[2]
        solution = find_start_times(C)
        self.assertTrue(check(C, solution, V))

    def test_04(self):
        C, V = tests[3]
        solution = find_start_times(C)
        self.assertTrue(check(C, solution, V))

    def test_05(self):
        C, V = tests[4]
        solution = find_start_times(C)
        self.assertTrue(check(C, solution, V))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)