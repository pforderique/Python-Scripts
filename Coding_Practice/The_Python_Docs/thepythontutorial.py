#Section 3.1.2: Strings
from os import linesep


def sec312():
    print('C:\some\name') #get rid of this by 
    print(r'C:\some\name') #using raw string

    print("""\
        Usage: thingy [OPTIONS]
            -h                        Display this usage message
            -H hostname               Hostname to connect to
        """) #EOL are included by default - use \ to prevent it

    text = ('Put several strings within parentheses '
            'to have them joined together.')
    print(text) #2 string literals next to each other are auto concat (does not with with variables or nums)

    #out of range slice indexes are handled gracefully (no error) when used for slicing:
    text = "piero"
    print(text[2:100])

#Section 4.3: Range function
def sec43():
    print(sum(range(1,11))) #RANGE IS AN ITERABLE - so we can pass it to funcs like sum
    print(list(range(0,101,2))) #we can also make a list! (evens from 0 to 100)

#Section 4.4: Break, Continue, and else
def sec44():
    #Loop statements may have an else clause;
    # it is executed when the loop ends, but not when the loop is terminated by a break statement.
    for i in range(1,6):
        for j in range(1,3):
            if i == j:
                print('i equals j equals ', i)
                break
        else:
            print("hey")
    #continue goes on to the next ieration
    #pass can be used for funcs, classes, and while statements

#Section 4.7: More on Functions (*args, **kwargs)
def sec47():
    # The default values are evaluated at the point of function definition
    
    def f(a, L=[]): #The default value is evaluated only once.
        L.append(a)
        return L
    print(f(1))
    print(f(2)) 
    print(f(3)) # so this will keep mutating list L

    # to avoid the above, do this instead:
    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L
    
    # PARAMETERS ARGS (just list out more "parameters" after kind - 
        # inputting a list will treat list like ONE arg unless you put * before it) 
        # args will be treated as tuple, so you can use it as an iterable input 
    # AND KWARGS (e.g. name='Piero') will be treated as a dict (infact, you can pass in a dict, but put ** before it)
    def cheeseshop(kind, *args, **kwargs):
        print("-- Do you have any", kind, "?")
        for arg in args:
            print(arg)
        print("-" * 40)
        for kw in kwargs:
            print(kw, ":", kwargs[kw])
    cheeseshop('pizza', 'its not Tuesday', "it's actually december "+str(4), name="Piero", age="19")

    # Restricting parameters to positional, standard, or keyword only
        #     >>> def standard_arg(arg):
        # ...     print(arg)
        # ...
        # >>> def pos_only_arg(arg, /):
        # ...     print(arg)
        # ...
        # >>> def kwd_only_arg(*, arg):
        # ...     print(arg)
        # ...
        # >>> def combined_example(pos_only, /, standard, *, kwd_only):
        # ...     print(pos_only, standard, kwd_only)

    # More examples
    def foo(name, **kwds): # pass in a dictionary for kwds
        for kw in kwds:
            print(kw, kwds[kw])
    myD = {"hey": 1, "there": 2}
    foo('piero', **myD)

    def foo2(*args): # *args is treated as an iterable (tuple) -- thus you can use sum 
        print(sum(args))
    foo2(1,2,3,4,5) # returns 1+2+3+4+5

        # Unpacking
    arguments = [1,11]
    outputList = list(range(*arguments)) # you can input lists with * before it in RANGE too!
    print(outputList)

    ### LAMBDA FUNCTIONS ###
    def make_incrementor(n):
        return lambda x: x + n
    f = make_incrementor(42)
    print( f(3) )# prints 45

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs) # prints [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

    ## DOCUMENTATION
    def myFunc(*args):
        '''Capitalized sentence that ends in period and breifly describes purpose.

        Since there are more lines in the doc string, we leave a space separating summary from rest of description.
        Now we spend 1-2 paragraphs describing the object’s calling conventions, its side effects, etc.
        '''
        pass
    print(myFunc.__doc__) #prints out description. Every thing will be tabbed except for first line (unless you also include it UNDER ''')

    ## ADDITIONAL COMMENTS: CODING STYLE PEP 8 ##

    # Use 4-space indentation, and no tabs.
    # Wrap lines so that they don’t exceed 79 characters.
    # Use blank lines to separate functions and classes, and larger blocks of code inside functions.
    # When possible, put comments on a line of their own.
    # Use docstrings.
    # Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
    # Name your classes and functions consistently; UpperCamelCase for classes and lowercase_with_underscores for functions and methods. 
    # Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
    # Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

#Section 5.1: LISTS - stacks, queues
def sec51():
    #List as STACK (FILO/LIFO)
    stack = [1,2,3]
    stack.append(4)
    stack.append(5)
    stack.pop() #pops/removes the last one appended! LIFO
    print(stack)

    #List as QUEUE (FIFO/LILO) - 
        # doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one
        # Use collections.deque - designed to have fast appends and pops from both ends
    from collections import deque # deque is a DOUBLE-ENDED QUEUE (generalized queue)
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    queue.popleft()                 # The first to arrive now leaves
    queue.popleft()                 # The second to arrive now leaves
    print(queue)                    # Remaining queue in order of arrival

#Section 5.4: SETS
def sec54():
    # Set operations
    a = set('fabrizzio')
    b = {x for x in 'orderique' if x not in 'qyz'} #can also do set comprehension!
    print(a)        # unique letters in a
    print(a - b)    # letters in a but not in b
    print(a | b)    # letters in a OR b OR both (OR)
    print(a & b)    # letters in BOTH a and b (AND)
    print(a ^ b)    # letters in a or b but NOT both (XOR)

#Section 5.6: Looping Techniques
def sec56():
    #dictionary looping
    d = dict(sape=4139, guido=4127, jack=4098) #same as d = {'sape': 4139, 'guido': 4127, 'jack': 4098}
    for key,val in d.items():
        print(key, val)

    #sequences (lists, tuples, strings)
    for idx, elem in enumerate(['tic', 'tac', 'toe']):
        print(idx, elem)

    #To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    #To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
    for i in reversed(range(1, 10, 2)):
        print(i)

    #To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for fruit in sorted(basket):
        print(fruit)
    print('-'*10)
    for fruit in sorted(set(basket)): #also use set to get unique values!!! Very idiomatic!
        print(fruit)

#Section 5.7: Conditionals
def sec57():
    #Remeber that AND and OR stop after one evaluates to True. E.g:
    string1, string2, string3 = '', 'piero', 'dance'
    non_null = string1 or string2 or string3
    print(non_null) #prints piero

    #Comparisons (Sec 5.8) that evaulate to True:
    # (1, 2, 3)              < (1, 2, 4)
    # [1, 2, 3]              < [1, 2, 4]
    # 'ABC' < 'C' < 'Pascal' < 'Python'
    # (1, 2, 3, 4)           < (1, 2, 4)
    # (1, 2)                 < (1, 2, -1)
    # (1, 2, 3)             == (1.0, 2.0, 3.0)
    # (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

#Section 6.0: Modules and Packages
def sec6():
    '''
    Presents what Modules are and how to format them.

    Ex: module.py
    '''
    #import fibo #cannot be resolved because it is looking for this in the ROOT project dirctory... you have this opened on PythonScripts
        # from fibo import fib, fib2    #this also works, however fibo would not be defined!
        # from fibo import *            #this imports all names except those beginning with an underscore (_). Try not to do this!
            # importing * from a module or package is frowned upon, since it often causes poorly readable code
    # fibo.fib(1000)
    # f = fibo.fib    #can also use your own variable
    # f(1000)

    '''
    Hierarchy:
        Looks for module first in ...
        1) built-in modules
        2) searches for a file named 'insertmodulename' in a list of directories given by the variable sys.path. sys.path
    '''

    #The built-in function dir([module]) is used to find out which names a module defines. It returns a sorted list of strings:
    # import fibo
    # print(dir(fibo))

    ### Modules and Packages ###
        # Just like the use of modules saves the authors of different modules from having to worry about 
        # each other’s global variable names, the use of dotted module names saves the authors of multi-module packages 
        # like NumPy or Pillow from having to worry about each other’s module names.
    '''
    sound/                      Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
    '''
    # The __init__.py files are required to make Python treat directories containing the file as packages.
    # Users of the package can import individual modules from the package, for example:
        #import sound.effects.echo OR from sound.effect import echo (better! bc now we can just refer to echo.echofilter(args))
    # Yet another variation is to import the desired function or variable directly:
        #from sound.effects.echo import echofilter (now we can just call echofilter(args) directly!)

    ## IMPORTING * FROM A PACKAGE ##
    #now what happens when the user writes from sound.effects import *?
        # importing every module in a package can take a LONG TIME, so 
        # the only solution is for the package author to provide an explicit index of the package
            # if a package’s __init__.py code defines a list named __all__, it is taken to be the 
            # list of module names that should be imported when from package import * is encountered.
                # For example, the __init__.py file in sound could include:
                    # __all__ = ["echo", "surround", "reverse"]

    '''
    You can also write relative imports:
    These imports use leading dots to indicate the current and parent packages involved in the relative import.

    from . import echo
    from .. import formats
    from ..effects import surround

    Note that relative imports are based on the name of the current module. 
    Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application 
    must always use absolute imports.
    '''

    '''
    Packages in Multiple Directories:
    Packages support one more special attribute, __path__. This is initialized to be a list 
    containing the name of the directory holding the package’s __init__.py before the code in that file is executed.
    '''

#Section 7.0: I/O - Formatting Strings
def sec7():
    #formatted string literals:
    name = "Piero"
    food = "pizza"
    print(f'My name is {name} and I like {food}')
    print('My name is {1} and I like {0}'.format(food, name))
    print(f'The value of pi is approximately {3.14159265:.3f}.')
    #Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
    #This is useful for making columns line up.
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')
    #Other modifiers can be used to convert the value before it is formatted. 
    #'!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
    animals = 'eels'
    print(f'My hovercraft is full of {animals}.')
    print(f'My hovercraft is full of {animals!r}.')
    #Can also format with DICTIONARY! Just use 0[key]
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 
            'Dcab: {0[Dcab]:d}'.format(table))
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)) #can also pass in dict with **
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    #Zfills
    print('12'.zfill(5))

    #For testing, convert any value to a string with the repr() or str() functions.

#Section 7.2: I/O - Files
def sec72():
    #It is good practice to use the with keyword when dealing with file objects. 
    myFile = r'C:\Users\fabri\OneDrive\Documents\DasText_and_Data\DasText\pyprac.txt'

    # with open(myFile) as f:
    #     howMuch = 30 #up to 30 chars (optional!)
    #     read_data = f.read(howMuch)
    #     print(read_data,'\n')

    # READING
    with open(myFile) as f:
        # line = f.readline()
        # print(line)
        # for line in f:
        #     print(line, end=' ')
        # print(f.readlines()) is the same as print(list(f)) -- list of all the lines
        pass

    # WRITING
    with open(myFile, 'a') as f:
        f.write('This is a test\n')
        for item in ["apple", 2, 4, 7]:
            f.write(str(item))
        print(f.tell()) #returns an integer giving the file object’s current position
        #to change the file object’s position, use f.seek(offset, whence)

    #JSON structured data
    import json
    x = [1, 'simple', 'list']
    json.dumps(x)
    with open(myFile, 'r+') as f:
        json.dump(x, f)




if __name__ == "__main__":
    sec72()