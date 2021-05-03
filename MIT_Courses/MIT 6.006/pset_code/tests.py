import unittest 
from inator_destroyer import inator_destroyer

tests = (
    (   
        (40,40,40),
        [((12,3,1),50),((36,4,7),10),((5,11,2),100)],
        110,
    ),
    (   
        (12,231,90),
        [((7, 7, 7),0), ((8, 6, 8),2), ((2, 12, 2),80), ((10, 4, 10),20), ((400,400,400),1000000000), ((4, 10, 4),32), ((11, 3, 11),23), ((5, 9, 5),30), ((6, 8, 6),10), ((3, 11, 3),70)],
        80,
    ),
    (
        (1000000000,1000000000,1000000000),
        [((9, 13, 11),1), ((11, 15, 13),1), ((10, 14, 12),1), ((3, 7, 5),1), ((6, 10, 8),1), ((5, 9, 7),1), ((7, 11, 9),1), ((4, 8, 6),1), ((2, 6, 4),1), ((8, 12, 10),1)],
        10,
    ),
    (
        (0,0,0),
        [((9, 13, 11),1), ((11, 15, 13),1), ((10, 14, 12),1), ((3, 7, 5),1), ((6, 10, 8),1), ((5, 9, 7),1), ((7, 11, 9),1), ((4, 8, 6),1), ((2, 6, 4),1), ((8, 12, 10),1)],
        0,
    ),
    (
        (70,80,90),
        [((53, 73, 97),3), ((79, 62, 95),131), ((83, 57, 92),890), ((67, 90, 98),2342), ((96, 75, 63),0), ((61, 66, 82),320), ((78, 65, 56),56), ((60, 87, 86),2), ((94, 70, 68),21), ((81, 54, 99),23)],
        376,
    ),
    (
        (150,300,200),
        [((107, 139, 125),232), ((138, 126, 193),2342), ((147, 169, 160),800), ((130, 194, 106),900), ((123, 192, 174),999), ((165, 159, 176),1001), ((102, 115, 124),423), ((197, 128, 129),32), ((151, 119, 118),649), ((177, 127, 141),930), ((120, 167, 191),86), ((140, 150, 132),890), ((188, 196, 186),803), ((145, 110, 104),89), ((189, 133, 180),20), ((156, 108, 185),21), ((101, 114, 121),55), ((134, 109, 158),11), ((135, 117, 182),5), ((112, 100, 166),48)],
        3469,
    ),
)


def is_okay(b1, b2):
    assert len(b1) == len(b2) == 3
    return all([b1[i] < b2[i] for i in range(3)])

def check(test):
    incinerator_size, incinerators, ans = test
    student_answer = inator_destroyer([b for b in incinerators],incinerator_size)

    student_answer = sorted([tuple(sorted(x)) for x in student_answer])
    evil_map = {tuple(sorted(b[0])):b[1] for b in incinerators}
    student_evil_potential = sum([evil_map[incinerator] for incinerator in student_answer])
    incinerator_size = tuple(sorted(incinerator_size))
    for i in range(len(student_answer)):
        if not is_okay(student_answer[i],incinerator_size):
            return False 
        if i > 0 and not is_okay(student_answer[i-1],student_answer[i]):
            return False
 
    return ans == student_evil_potential



class TestClass(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))
    def test_06(self): self.assertTrue(check(tests[ 5]))



if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)

