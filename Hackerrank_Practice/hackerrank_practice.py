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

#returns minimum value of absolute difference of the sum of the 
# 2 nodes formed when cut at a certain edge
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

# data = [100, 200 ,100, 500, 100, 600]
data = [205, 573, 985 ,242, 830, 514, 592, 263 ,142, 915]
# edges = [(1, 2),(2, 3),(2, 5),(4, 5),(5, 6)]
edges = [(2,8),(10,5),(1,7),(6,9),(4,3),(8,10),(5,1),(7,6),(9,4)]
cutTheTree(data,edges)