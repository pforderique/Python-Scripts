# Arrays and Strings (Ch1)
# Piero Orderique
# Started technically in Sep 2020
# Came back to try practice probs

# Want to build a string of words each x letters long?
wordlist = []
max = 200
with open(r'C:\Users\fabri\OneDrive\Documents\DasText_and_Data\DasText\1000_most_common_words.txt') as f:
    count = 0
    for word in f:
        wordlist.append(word[:-1])
        count+=1
        if count == max: break

# BAD WAY :
    # O(xn^2) time because we have to keep copying words
def join_words(words=wordlist):
    sentence = ''
    for word in words:
        sentence += word
    return sentence

# FASTER WAY :
    # Use "String Builder" to append words and only convert to string at end
    # instead of string builder from java, ill use .join
def join_words_fast(words=wordlist):
    sentence = []
    for word in words:
        sentence.append(word)
    return ''.join(sentence)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit(join_words))
    print(timeit.timeit(join_words_fast))
