from random import randint
import sys

answer = randint(1,10) 

attempt = 0 
while True:
    try:
        attempt += 1
        if attempt == 1:
            guess = int(input('Geuss number between 1~10:  '))
        elif 5 >= attempt >= 2:
            guess = int(input('Wrong! Guess one more time:   '))
        elif 9 >= attempt >= 6:
            guess = int(input('Really? You need to try harder:   '))
        elif attempt >= 10:
            guess = int(input('OMG? You are so unlucky:   '))

        if 0 < guess < 11:
            if guess == answer:
                print("----------------------------------------------------")
                print(f'Great! You were able to guess number after {attempt} attempts')
                break
        else:
            print('Hey mate, I said between 1~10')

    except ValueError:
        print('please enter the number')
