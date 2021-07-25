def upsample(x,p):
    if type(p) != int or p < 1: return []

    res = [0]*len(x)*p
    num_between = p - 1
    curr_idx = 0

    # Between any two samples x[n] and x[n+1] in the original signal, we will add in p-1 new samples via interpolation
    for i in range(len(x) - 1):
        dy = (x[i+1] - x[i])/p

        # insert x[n]
        res[curr_idx] = x[i] 
        curr_idx += 1
        # interpolate
        for multiplier in range(1, num_between + 1):
            res[curr_idx] = x[i] + multiplier*dy
            curr_idx += 1

    # insert last element
    res[curr_idx] = x[-1]
    curr_idx += 1

    # extrapolate! add in p - 1 more signals
    slope = (x[-1] - x[-2])/p
    for multiplier in range(1, num_between + 1):
        res[curr_idx] = x[-1] + multiplier*slope
        curr_idx += 1

    return res

def downsample(x,q):
    if type(q) != int or q < 1: return []

    res = []

    for i in range(0, len(x), q):
        res.append(x[i])

    return res

def resample(inp,desired_length):
    LCM = lcm(desired_length, len(inp))

    p = LCM//len(inp)
    q = LCM//desired_length

    print(p,q)

    upsampled = upsample(inp, p)
    print(upsampled)
    
    # return downsample(upsample(inp, p), )

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# print(upsample([0, 3, 6], 3))
# print(downsample([0, 1.0, 2.0, 3, 4.0, 5.0, 6, 7.0, 8.0], 3))
# print(resample([0, 3, 6], 3))

def caesar_cipher(message,shift,encrypt):
    res = ""

    if encrypt:
        for char in message:
            # get idx and shift it
            idx = ord(char)
            new_idx = (idx - 32) + shift
            # print(new_idx)
            if new_idx >= 95: new_idx = new_idx%25 + 65
            else: new_idx += 32
            # print(f"{char}: {idx} -> {chr(new_idx)}: {new_idx}")
            res += chr(new_idx)
        return res

    else:
        for char in message:
            # get idx and shift it
            idx = ord(char)
            new_idx = (idx - 65) - shift
            # print(new_idx)
            if new_idx < 0 : new_idx = new_idx%25 + 65
            else: new_idx += 65
            # print(f"{char}: {idx} -> {chr(new_idx)}: {new_idx}")
            res +=  chr(new_idx)
        return res

# print(caesar_cipher("abc", 4, False))
# print(caesar_cipher("{|}~", 4, True))
# print(caesar_cipher(" !#", 4, False))
# print(caesar_cipher("RZA, GZA, Old Dirty Bastard, Inspectah Deck, Raekwon the Chef, U-God, Ghostface Killah, and the Method Man",6,True))

def vigenere_cipher(message,keyword,encrypt):
    res = ""

    keyword_idx = 0
    for char in message:
        shift_char = keyword[keyword_idx]
        shift = ord(shift_char) - 32
        keyword_idx = (keyword_idx+1)%len(keyword)
        res += caesar_cipher(char, shift=shift, encrypt=encrypt)
    return res

# print(vigenere_cipher("abc", ' !"', False))
print(caesar_cipher("UIABMZ, Q LMTQDMZ BPM ATIGMZ. APM EPW GWC UWAB LMAQZM. AWZZG -- EPWU", 8, False))