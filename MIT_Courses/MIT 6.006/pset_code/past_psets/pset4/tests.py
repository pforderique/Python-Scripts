import unittest
from PatientDatabase import PatientDatabase
# from dbtesting import PatientDatabase

draw = True # CHANGE TO TRUE FOR VISUAL OUTPUT

tests = (
    (
        (("a",10), ("b",4), ("c", 9), ('q', 3, 6),('q', 2, 21)),
        [1,3],
    ),
    (
        (("Fineas",10), ("Pherb",6), ("Agent B",8), ("Dr. Hoofenschmirtz",9), ("Lindana",5), ('q', 1, 9),('q', 3, 9),("",9),('q', 1, 2)),
        [4,4,0],
    ),
    (
        (("Percy Jackson",15), ("Anabeth Chase",12), ("Nico di Angelo",7), ("Luke Castellan",11), ("Thalia Grace",17), ("Bianca di Angelo",14), ("Grover Underwood",18), ("Clarissa LaRue",11), ("Chiron",2), ("Tyson",4), ('q', 6, 15),('q', 2, 12),('q', 9, 30),('q',100,1001)),
        [5,5,6,0],
    ),
    (
        (("Cody Martin",31), ("London Tipton",25), ("Zach Martin",33.231), ("Esteban",38), ("Arwin",50), ("Marion Moseby",40), ("Maddie Fitzpatrick",46), ("Carey Martin",9), ("Muriel",45), ("Zack Martin's twin",31), ('q', 1, 49),('q', 8, 49), ("Hannah Montana",41),("Miley Cyrus",41), ("Rico",43), ("Lily",47), ("Jackson",11), ("Oliver",35), ("Robby Steward",8), ("Billy Ray Cyrus",21), ("Alex",21), ("Justin",48), ("Max",26), ('q', 11, 28),('q', 13, 50)),
        [8, 8, 4, 15],
    ),
    (
        (("a",70.5), ("b",80.1), ("c",85.9823), ("d",81), ("e",27.001), ("f",62.3223), ("g",87.2310), ("h",75.2320492), ("i",41.01), ("j",11.999), ("k",90.2380), ("l",13.231), ("m",52.29023), ("n",21.3284), ("o",57.555), ('q', 5, 27),('q', 8, 100), ('q', 54, 73),('q', 0, 4), ("p",99), ("r",16), ("s",90.1), ("t",60), ("u",22.3242), ("v",99), ("w",76.2342), ("x",6), ("y",44.0923), ("z",75), ("aa",76), ("bb",81.001), ("cc",73.001), ("dd",43), ("ee",39), ('q', 64, 71),('q', 64, 1210133242432423), ('q', 45, 82),('q', 42, 90)),
        [3, 15, 3, 0, 1, 14, 13, 17],
    ),
    

)

def check(test):
    ops, ans = test
    database = PatientDatabase() 
    i = 0
    for op in ops:
        
        if draw: 
            print('\nDatabase: \n%s\n' % database)
        if op[0] == 'q':
            _, t1, t2 = op
            sol = database.num_patients(t1, t2)
            if draw: 
                print(' our num_patients(%s,%s): %s' % (t1, t2, ans[i]))
                print('your num_patients(%s,%s): %s' % (t1, t2, sol))
            if sol != ans[i]:
                ans.append(sol)
                return False
            i += 1
        else:
            name,priority = op
            database.update_patient(name,priority)
            if draw: 
                print("update_patient(%s,'%s')" % (name,priority))
    return True

class TestNumPatients(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)