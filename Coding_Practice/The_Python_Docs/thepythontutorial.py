#Section 3.1.2: Strings
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


if __name__ == "__main__":
    sec51()