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