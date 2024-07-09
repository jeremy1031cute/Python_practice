import random


def main():
    num_digit = 3
    max_guesses = 10
    print('''Bagels , a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
    Pico       One digit is correct but in the wrong position.
    Fermi      One digit is correct and in the right position.
    Bagels     No digit is correct.'''.format(num_digit))
    while 1:
        print('I have thought up a number.')
        serect_num = get_serect_num(num_digit)
        print(serect_num)
        print('You have {} guesses to get it.'.format(max_guesses))
        
        guess_times = 1
        while guess_times <= max_guesses:
            guess = ''
            #ensure guess is vaild
            while (len(guess) != num_digit) or (not guess.isdecimal()):
                print('Guess #{}'.format(guess_times))
                guess = input('input: ')
            
            clues = get_clues(guess,serect_num)
            print(clues)
            guess_times += 1
            
            if guess == serect_num:
                break
            if guess_times > max_guesses:
                print('You ran out of guesses');
                print('The answer was {}.'.format(serect_num))
        print('Do you want to play again(yes or no)')
        if not input('input: ').lower().startswith('y'):
            break       
    print('Thanks for playing!')
    
    
def get_serect_num(num_digits):
    num_arr = list('0123456789') #num_arr = list(range(10))
    random.shuffle(num_arr)
    
    serect_num = ''
    for i in range(num_digits):
        serect_num += str(num_arr[i])
        
    return serect_num

def get_clues(guess,serect_num):
    if guess == serect_num:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == serect_num[i]:
            clues.append('Fermi')
        elif guess[i] in serect_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
        
    print('Bagels')
    
main()