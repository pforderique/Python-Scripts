LOWER = 0
UPPER = 100

print('Please think of a number between %s and %s!' % (LOWER, UPPER))
while True:
    guess = int((LOWER+UPPER)/2)
    print('Is your secret number %s?' % guess)
    answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if answer == 'h':
        UPPER = guess
    elif answer == 'l':
        LOWER = guess
    elif answer == 'c':
        print('Game over. Your secret number was:', guess)
        break
    else:
        print('Sorry, I did not understand your input.')