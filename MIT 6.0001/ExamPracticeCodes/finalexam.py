trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    if int(us_num) < 11:
        return trans[us_num]
    elif int(us_num) < 20:
        return 'shi '+trans[us_num[1]]
    else:
        tens_digit = us_num[0]
        ones_digit = us_num[1]
        answer = ''
        if int(ones_digit) != 0:
            return trans[tens_digit] + ' shi '+trans[ones_digit]
        else:
            return trans[tens_digit] + ' shi'

# print(convert_to_mandarin('36')) #will return san shi liu)

def longest_run1(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here

    #find longest increasing 
    list_of_inc = []
    longest_inc = []
    for i in range(1, len(L)):
        if L[i] >= L[i-1]:
            longest_inc.append(L[i-1])
            # if we are at the last one, go ahead and append the last term too if its bigger.
            if (L[i] >= L[i-1] and i < len(L)-1 and L[i+1] < L[i]):
                longest_inc.append(L[i])
        else:
            list_of_inc.append(longest_inc)
            longest_inc = []
    list_of_lens = [len(sublist) for sublist in list_of_inc]
    longest_inc = list_of_inc[list_of_lens.index(max(list_of_lens))]

    #find longest decreasing
    list_of_dec = []
    longest_dec = []
    for i in range(1, len(L)):
        if L[i] <= L[i-1]:
            longest_dec.append(L[i-1])
            # if we are at the last one, go ahead and append the last term too if its bigger.
            if (L[i] <= L[i-1] and i < len(L)-1 and L[i+1] > L[i]):
                longest_dec.append(L[i])
        else:
            list_of_dec.append(longest_dec)
            longest_dec = []
    list_of_lens = [len(sublist) for sublist in list_of_dec]
    longest_dec = list_of_dec[list_of_lens.index(max(list_of_lens))]

    if len(longest_inc) >= len(longest_dec):
        return sum(longest_inc)
    else:
        return sum(longest_dec)
    
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here

    dec_count = 0
    inc_count = 0
    maxcount = 0
    result = 0

    for char in range(len(L) - 1):
        if (L[char] <= L[char + 1]):
            dec_count += 1
            if dec_count > maxcount:
                maxcount = dec_count
                result = char + 1
        else:
            dec_count = 0
        if (L[char] >= L[char + 1]):
            inc_count += 1            
            if inc_count > maxcount:
                maxcount = inc_count
                result = char + 1
        else:
            inc_count = 0
        
    startposition = result - maxcount
    return sum(L[startposition:result + 1])

# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# print(longest_run(L))

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name +' says: It is obvious that '+Lecturer.lecture(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')
# print(pe.say('the sky is blue'))  #Prof. eric says: I believe that eric says: the sky is blue 
# print(ae.say('the sky is blue'))  #Prof. eric says: It is obvious that I believe that eric says: the sky is blue 

#########   RETURNING  A  FUNCTION!!!!
x=10
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE 
    def func(x):
        L_copy = L[:]
        L_copy.reverse()
        result = 0
        for i in range(len(L_copy)):
            result += L_copy[i]*(x**i)
        return result
    return func

# print(general_poly([1, 2, 3, 4])(10))

wordList = ['word','apple','tree']
lStr = ['adwfsroc']

##returns max sum of longest consecutive sum 
## [1,2,3] returns 6
## [-1,-1, 1,0] returns 1

# def getMaxConsec(L):
#     all_lists = []
#     for i in range(len(L)):
#         for j in range(i+1,len(L)+1):
#             all_lists.append(L[i:j])

#     cons_list = []
#     for sublist in all_lists:
#         print('this sublist',sublist,' must be',list(range(min(sublist), max(sublist)+1)))
#         if list(set(sublist)) == list(range(min(sublist), max(sublist)+1)) or sublist == list(range(max(sublist), min(sublist)+1)):
#             cons_list.append(sublist)
    
#     sums_list = [sum(e) for e in cons_list]
#     print(all_lists, '      ',cons_list,'      ',sums_list)

# L = [-1,-1, 1,0]
# getMaxConsec(L)
    
# def hasConsecutives(L):
#     sublists = []
#     for i in range(len(L)):
#         for j in range(i+1,len(L)+1):
#             sublists.append(L[i:j])
#     hasCons = True
#     for sub in sublists:
#         iamcons = True
#         if len(sub) != 1:
#             ordered = list(range(min(sub), max(sub)+1))
#             #CHECKS IF ONE LIST CONTAINS THE OTHER
#             for idx in range(len(ordered) - len(sub)+1):
#                 for j in range(len(sub)):
#                     if sub[j] != ordered[idx+j]:
#                         iamcons = False
#             if iamcons:
#                 return iamcons
                        
#                 print(sub, ordered)

#     return hasCons

# L = [6,2,5,10,2]
# print(hasConsecutives(L))