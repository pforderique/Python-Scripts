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



if __name__ == "__main__":
    sec312()