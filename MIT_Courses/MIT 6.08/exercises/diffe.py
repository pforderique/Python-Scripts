
def keyword_generate(inputt):
    string = str(inputt)
    res = ''
    for char in string:
        res += chr(int(char))

    return res


def dhke1(t,p,m,a,message_in, encrypt):
    if encrypt:
        # generate the key with your a:
        num_key = int(pow(m,a,p)) 
        # get the keyword
        keyword = keyword_generate(num_key)

        return vigenere_cipher(message_in, keyword, encrypt=encrypt)

    # else decrypt
    else:
        # generate key from their t:
        num_key = int(pow(t, a, p))
        # get keyword
        keyword = keyword_generate(num_key)

        return vigenere_cipher(message_in, keyword, encrypt)


def dhke(t,p,m,a,message_in, encrypt):
    num_key = pow(t, a, p)

    # get the keyword
    keyword = keyword_generate(num_key)

    return vigenere_cipher(message_in, keyword=keyword, encrypt=encrypt)



def vigenere_cipher(message,keyword,encrypt):
    return 'hey'
#     res = ""

#     keyword_idx = 0
#     for char in message:
#         shift_char = keyword[keyword_idx]
#         shift = ord(shift_char) - 32
#         keyword_idx = (keyword_idx+1)%len(keyword)
#         res += caesar_cipher(char, shift=shift, encrypt=encrypt)
#     return res

if __name__ == "__main__":
    print(keyword_generate(1342))
