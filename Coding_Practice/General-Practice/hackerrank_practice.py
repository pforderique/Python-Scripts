#Converts between standard and military time 
def timeConversion(s):
    '''
    s is a standard time string in format HH:MM:SSAM
    returns military time in format HH:MM:SS
    '''
    doyoulikeAMMorFMMMM = s[len(s)-2:len(s)]
    hours = '00'
    if doyoulikeAMMorFMMMM == 'AM':
        hr = int(s[0:2])%12
        if hr < 10: hours = '0'+str(hr)
        else: hours = str(hr)
    else:
        hours = str(12+int(s[0:2])%12)
    return hours+s[2:len(s)-2]

#returns minimum value of abs. difference of the sum of the 2 nodes formed when cut at a certain edge
def cutTheTree(data, edges):
    def sumsWnode(node, edges):
        mSum = 0
        if len(edges) == 0:
            return sum
        for i,tup in enumerate(edges):
            copy = edges[:]
            n1 = tup[0]
            n2 = tup[1]
            del copy[i]
            if n1 == node: mSum += data[n2-1]+sumsWnode(n2, copy)
            elif n2 == node: mSum += data[n1-1]+sumsWnode(n1, copy)
        return mSum
    diffs = []
    for i, tup in enumerate(edges):
        copy = edges[:]
        a = tup[0]
        b = tup[1]
        del copy[i]
        sum1 = data[a-1] + sumsWnode(a, copy)
        sum2 = data[b-1] + sumsWnode(b, copy)
        print('cut at ',i,': sum1 = ',sum1,' sum2 = ',sum2,' diff = ',abs(sum1-sum2))
        diffs.append(abs(sum1-sum2))
    return min(diffs)
    # # data = [100, 200 ,100, 500, 100, 600]
    # data = [205, 573, 985 ,242, 830, 514, 592, 263 ,142, 915]
    # # edges = [(1, 2),(2, 3),(2, 5),(4, 5),(5, 6)]
    # edges = [(2,8),(10,5),(1,7),(6,9),(4,3),(8,10),(5,1),(7,6),(9,4)]
    # cutTheTree(data,edges)

#Grading Students
def gradingStudents(grades):
    out = []
    for idx,grade in enumerate(grades):
        if grade < 38:
            print(grade)
            out.append(grade) 
        elif grade%5 > 2:
            print(str(grade+5-(grade%5)))
            out.append(grade+5-(grade%5))
        else:
            print(grade)
            out.append(grade) 
    return out

#Apple and Orange
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    >>> countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
    1
    1
    """
    print(sum([1 for apple in apples if (a+apple) >= s and (a+apple) <= t]))
    print(sum([1 for orange in oranges if (b+orange) >= s and (b+orange) <= t]))

#Counting Valleys
def countingValleys(steps, path):
    stepDict = {"D":-1, "U":1}
    totalValleys = 0
    lastStep = 0
    for char in path:
        current = lastStep + stepDict[char]
        if lastStep < 0 and current == 0:
            totalValleys += 1
        lastStep = current
    return totalValleys
    # print(countingValleys(8,'DDDUUDUUUDDU'))

#Left Rotation
def rotateLeft(d, arr):
    arrprime = [0]*len(arr)
    for i in range(len(arr)):
        arrprime[(i-d)%len(arr)] = arr[i]
    return arrprime
    # print(rotateLeft(2,[1,2,3,4,5]))

#Sparse Arrays - assuming no repeating queries
def matchingStringss(strings, queries):
    result = []
    for q in queries:
        total = 0
        i = 0
        while i < len(strings):
            print(q,i,strings, "total:",total)
            if q == strings[i]:
                total += 1
                strings.pop(i)
                i-=1
            i+=1
        result.append(total)
    return result
def matchingStrings(strings, queries):
    result = []
    for q in queries:
        total = 0
        for s in strings:
            if q == s:
                total+=1
        result.append(total)
    return result
    print(matchingStrings(['ab','ab','abc'], ['ab','abc','bc']))

#Balanced Sum - Salesforce: PASSED
def balancedSum(arr):
    LHS = arr[0]
    RHS = sum(arr[2:])
    for i in range(1, len(arr)-1):
        if LHS == RHS:
            return i
        else:
            LHS += arr[i]
            RHS -= arr[i+1]
    return -1

#Sort Intersect - Salesforce: PASSED
def sortIntersect(volcanic, nonVolcanic):
    result = []
    for vol in volcanic:
        try:
            result.append(nonVolcanic.pop(nonVolcanic.index(vol)))
        except:
            pass
    result.sort(reverse=True)
    return result

#doctest
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

